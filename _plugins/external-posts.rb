require 'feedjira'
require 'httparty'
require 'jekyll'

module ExternalPosts
  class ExternalPostsGenerator < Jekyll::Generator
    safe true
    priority :high

    def generate(site)
      Array(site.config['external_sources']).each do |src|
        Jekyll.logger.info "External posts:", "Fetching #{src['name']}"

        begin
          response = HTTParty.get(
            src['rss_url'],
            timeout: 10,
            headers: { 'User-Agent' => 'canererden.com Jekyll feed reader' }
          )
          raise "HTTP #{response.code}" unless response.success?

          feed = Feedjira.parse(response.body)
          raise 'Feed could not be parsed' unless feed

          feed.entries.each do |entry|
            next if entry.title.to_s.empty? || entry.url.to_s.empty?

            slug = entry.title.downcase.strip.gsub(' ', '-').gsub(/[^\w-]/, '')
            path = site.in_source_dir("_posts/#{slug}.md")
            doc = Jekyll::Document.new(
              path, site: site, collection: site.collections['posts']
            )
            doc.data['external_source'] = src['name']
            doc.data['feed_content'] = entry.content
            doc.data['title'] = entry.title
            doc.data['description'] = entry.summary
            doc.data['date'] = entry.published
            doc.data['redirect'] = entry.url
            site.collections['posts'].docs << doc
          end
        rescue StandardError => e
          Jekyll.logger.warn "External posts:", "Skipping #{src['name']} (#{e.message})"
        end
      end
    end
  end

end
