REPO = kartychak/group25082026


.PHONY: hello
hello:
	echo '11111111111'
	echo '222222222222'
	@echo '333333333333'


.PHONY: step2
step2: hello
	echo '*************'
	echo '-----------'
	@echo '+++++++++++++++'


.PHONY: build
build:
    # make build v=0.6.0
	docker build  -t $(REPO):$(v) -t $(REPO):latest .
	docker push  $(REPO):$(v)
	docker push  $(REPO):latest