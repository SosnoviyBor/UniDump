FROM nginx:alpine

COPY . /vagrant_data

 CMD cat /vagrant_data/index_template.html > /usr/share/nginx/html/index.html && \
 ifconfig eth0 >> /usr/share/nginx/html/index.html && \
 echo "</body></html>" >> /usr/share/nginx/html/index.html && \
 nginx -g 'daemon off;'