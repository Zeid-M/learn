---
To push a new tag in Docker and make it the `latest` tag, follow these steps:

### 1. **Tag the image with a new version and latest**
```sh
docker tag my-image:old-tag my-image:new-tag
docker tag my-image:new-tag my-image:latest
```
Or if you're building a new image:
```sh
docker build -t my-image:new-tag -t my-image:latest .
```

### 2. **Push both the new tag and `latest` tag**
```sh
docker push my-image:new-tag
docker push my-image:latest
```

### 3. **If using a remote registry (e.g., Docker Hub, AWS ECR, GCR, etc.)**
Make sure you're tagging with the full registry path:
```sh
docker tag my-image:new-tag my-registry/my-image:new-tag
docker tag my-image:new-tag my-registry/my-image:latest

docker push my-registry/my-image:new-tag
docker push my-registry/my-image:latest
```

### 4. **Verify that the tags are updated**
List the tags on Docker Hub or your registry to confirm:
```sh
docker images | grep my-image
```

---
