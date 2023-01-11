FROM centos:8

# ML8
RUN curl -OL https://repo.dist.miraclelinux.net/miraclelinux/migration-tool/migrate2ml.sh && \
    chmod +x migrate2ml.sh
RUN ./migrate2ml.sh --minimal


RUN dnf -y update && \
    dnf -y install gcc make httpd httpd-devel pkgconfig libcap-devel wget unzip redhat-rpm-config mod_php && \
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

# virtual setting
RUN mkdir -p /var/www/modtest.example.jp/Web/cgi-bin/
RUN mkdir -p /var/www/modtest.example.jp/Web/htdocs/

COPY htdocs/index.html /var/www/modtest.example.jp/Web/htdocs/
COPY htdocs/info.php /var/www/modtest.example.jp/Web/htdocs/
COPY cgi-bin/makefile.cgi /var/www/modtest.example.jp/Web/cgi-bin/
COPY cgi-bin/sleep.cgi /var/www/modtest.example.jp/Web/cgi-bin/

# user setting
RUN groupadd -g 20000 moduser && \
    useradd  -u 20000 -g moduser moduser && \
    chown -R moduser.moduser /var/www/modtest.example.jp/Web/htdocs && \
    chown -R moduser.moduser /var/www/modtest.example.jp/Web/cgi-bin && \
    chmod 755 /var/www/modtest.example.jp/Web/cgi-bin/makefile.cgi && \
    chmod 755 /var/www/modtest.example.jp/Web/cgi-bin/sleep.cgi


# mod_process_security - v1.2.0
RUN pushd /usr/local/src/ && \
    wget -O mod_process_security_v1_2_0.zip https://github.com/matsumotory/mod_process_security/archive/refs/tags/v1.2.0.zip && \
    unzip mod_process_security_v1_2_0.zip && \
    pushd mod_process_security-1.2.0 && \
    apxs -i -c -l cap mod_process_security.c && \
    popd && \
    rm -f mod_process_security_v1_2_0.zip && \
    popd

COPY conf.d/process_security.conf /etc/httpd/conf.d/

EXPOSE 8082

CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
