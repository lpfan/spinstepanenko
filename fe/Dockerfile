FROM nginx:latest

RUN apt-get update
RUN apt-get install -y curl gnupg git apt-transport-https

RUN curl -sL https://deb.nodesource.com/setup_8.x -o | bash -
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y nodejs yarn

RUN rm -v /etc/nginx/nginx.conf


ADD . /opt/spinstepannenko/fe
VOLUME ["/opt/spinstepanenko/fe"]
WORKDIR /opt/spinstepannenko/fe

ADD config/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
