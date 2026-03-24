FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

# Remove stale Yarn apt repo that has an expired GPG key
RUN rm -f /etc/apt/sources.list.d/yarn.list 2>/dev/null; \
    rm -f /usr/share/keyrings/yarn-keyring.gpg 2>/dev/null; \
    true
