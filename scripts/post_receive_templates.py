


def replace_template(tempdir, project_path, git_dir_path):
 return \
f'''
# create a post-receive file
#!/bin/bash
# generated automatically

# Deploy the content to the temporary directory
mkdir -p {tempdir}
mkdir -p {project_path}
git --work-tree={tempdir} --git-dir={git_dir_path} checkout -f || exit;

rm -rf {project_path}/*
cp -r {tempdir}/* {project_path} || exit;
rm -rf {tempdir} || exit;
cd {project_path} || exit;

# create a Dockerfile 
# add multiline string to a file
cat <<EOF > {project_path}/Dockerfile
FROM node:14 AS builder
WORKDIR /app
COPY . .
RUN npm install && npm run build

FROM nginx:alpine
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=builder /app/build .
ENTRYPOINT ["nginx", "-g", "daemon off;"]
EOF

docker build -t react-nginx .;
docker run -d -p 3000:80 react-nginx;
# kubectl apply -f {project_path}/k8s.yaml;


'''  
