createcluster:
	kind create cluster
build:
	docker build -t servicex-did-finder-demo .
load:
	kind load docker-image servicex-did-finder-demo:latest
servicex:
	helm delete pondd-servicex
	helm install -f values_minimal.yaml --version v1.0.17 pondd-servicex ssl-hep/servicex
forward:
	kubectl get pods --namespace default -l "app=pondd-servicex-servicex-app" -o jsonpath="{.items[0].metadata.name}" > POD_NAME
	kubectl port-forward `cat POD_NAME` 5000:5000
test:
	python tests/post.py
deletecluster:
	kind delete cluster
