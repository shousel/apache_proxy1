# Front Web Container
- OS：MIRACLE LINUX 8.4
- Kernel：4.18.0-305.el8.x86_64
- Web：httpd-2.4.37-51.module+el8+1548+a2ac2845.ML.1.x86_64
  - MPM：eventMPM

# Back Web Container
- OS：MIRACLE LINUX 8.4
- Kernel：4.18.0-305.el8.x86_64
- Web：httpd-2.4.37-51.module+el8+1548+a2ac2845.ML.1.x86_64
  - MPM：preforkMPM
  - mod_process_security：v1.2.0（https://github.com/matsumotory/mod_process_security）

# docker-compose
1. build
```
# docker-compose build
```
2. up
```
# docker-compose up -d
```
