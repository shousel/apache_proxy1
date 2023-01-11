FROM centos:8

# ML8
RUN curl -OL https://repo.dist.miraclelinux.net/miraclelinux/migration-tool/migrate2ml.sh && \
    chmod +x migrate2ml.sh
RUN ./migrate2ml.sh --minimal


RUN dnf -y update && \
    dnf -y install gcc make httpd httpd-devel pkgconfig libcap-devel wget unzip redhat-rpm-config && \
    dnf clean all && \
    rm -rf /var/cache/dnf

# apache setting
COPY conf/httpd.conf /etc/httpd/conf/
COPY conf.modules.d/00-mpm.conf /etc/httpd/conf.modules.d/
COPY conf.modules.d/00-dav.conf /etc/httpd/conf.modules.d/
COPY conf.modules.d/00-proxy.conf /etc/httpd/conf.modules.d/
COPY conf.modules.d/10-proxy_h2.conf /etc/httpd/conf.modules.d/
COPY conf.modules.d/10-h2.conf /etc/httpd/conf.modules.d/
COPY conf.d/mpm.conf /etc/httpd/conf.d/

EXPOSE 80

CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
