


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
# Name the node stage "builder"
FROM node:14 AS builder
# Set working directory
WORKDIR /app
# Copy all files from current directory to working dir in image
COPY . .
# install node modules and build assets
RUN npm install && npm run build

# nginx state for serving content
FROM nginx:alpine
# Set working directory to nginx asset directory
WORKDIR /usr/share/nginx/html
# Remove default nginx static assets
RUN rm -rf ./*
# Copy static assets from builder stage
COPY --from=builder /app/build .
# Containers run nginx with global directives and daemon off
ENTRYPOINT ["nginx", "-g", "daemon off;"]
EOF

# docker build -t react-nginx .;
# kubectl apply -f {project_path}/k8s.yaml;


'''  
