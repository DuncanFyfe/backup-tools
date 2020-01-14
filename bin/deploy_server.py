#!/usr/bin/env python3
import json
import os
import sys

from jinja2 import Environment, PackageLoader, Template, select_autoescape

import backup_tools
import servercfg


def load_srvcfg(prefix=""):

    cfgsections = [
        ("users", "users.json"),
        ("secrets", "secrets.json"),
        ("minios", "minios.json"),
        ("nginx", "minios.json"),
    ]
    cfg = {}
    for cs in cfgsections:
        filename = os.path.join(prefix, cs[1])
        if os.path.exists(filename):
            with open(filename, "r") as r:
                cfg[cs[0]] = json.load(r)
        else:
            cfg[cs[0]] = {}
    for mid, m in cfg["minios"].items():
        uid = m.get("uid", None)
        if uid in cfgin["users"]:
            m["user"] = users["uid"]
        if uid in cfgin["secrets"]:
            m["secrets"] = secrets["uid"]
    cfg.pop("users")
    cfg.pop("secrets")
    return cfg


def minio_env(env, dest, m):
    tpl = env.get_template("minio.env.j2")
    mid = m["id"]
    txt = tpl.render(minio=m)
    filename = f"{dest}/minio{mid}.env"
    with open(filename, "w") as w:
        w.write(txt)


def nginx_env(env, dest, n):
    tpl = env.get_template("nginx.env.j2")
    txt = tpl.render(nginx=n)
    filename = f"{dest}/nginx.env"
    with open(filename, "w") as w:
        w.write(txt)


def nginx_config(env, dset, c):
    tpl = env.get_template("nginx.conf.j2")
    txt = tpl.render(nginx=c)
    filename = f"{dest}/nginx.conf"
    with open(filename, "w") as w:
        w.write(txt)


def docker_compose(env, dest, nginx, minio, ssl):
    tpl = env.get_template("docker-compose.yml.j2")
    txt = tpl.render(nginx=nginx, minio=minio, ssl=ssl)
    filename = f"{dest}/docker-compose.yml"
    with open(filename, "w") as w:
        w.write(txt)


def main():
    srvcfg = load_srvcfg()
    users = srvcfg["users"]
    minios = srvcfg["minios"]
    nginxcfg = srvcfg["nginx"]
    sslcfg = srvcfg["sslcfg"]
    nginxcfg["minio_ports"] = [u["port"] for u in users]
    for u in users:
        minio_env(env, dest, u)

    nginx_env(env, dest, nginxcfg)
    for m in minios:
        u = users.get(m["id"], {})
        minio_env(env, dest, m, u)

    env = Environment(
        loader=PackageLoader("backup_tools", "templates"), autoescape=False
    )
    minios_tpl = env.get_
    for u in users:
        if u["backup"]:
            pass

    minios = []


def cli_main():
    pass


if __name__ == "__main__":
    main()
