# We need ruby 3.1.0. I found this from Docker Hub
FROM ruby:3.1.0

EXPOSE 3000

WORKDIR /usr/src/app

# Install the correct bundler version
RUN gem install bundler:2.3.3

# Copy the files required for dependencies to be installed
COPY Gemfile* ./

# Install all dependencies
RUN bundle install

# Copy all of the source code
COPY . .

# Run database migrations
RUN rails db:migrate RAILS_ENV=production

# Precompile assets
RUN rake assets:precompile

# Run the application
CMD ["rails", "s", "-e", "production"]
