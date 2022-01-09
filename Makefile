.PHONY: list

list:
	@LC_ALL=C $(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

createcluster:
	kind create cluster

build:
	docker build -t servicex-did-finder-demo .

load:
	kind load docker-image servicex-did-finder-demo:latest

servicex:
	helm install -f values_minimal.yaml --version v1.0.17 pondd-servicex ssl-hep/servicex

demo:
	kubectl create -f deploy.yaml

forward:
	kubectl get pods --namespace default -l "app=pondd-servicex-servicex-app" -o jsonpath="{.items[0].metadata.name}" > POD_NAME
	kubectl port-forward `cat POD_NAME` 5000:5000

test:
	python tests/post.py

servicexstop:
	helm delete pondd-servicex

deletecluster:
	kind delete cluster
