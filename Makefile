requirements:
	pip freeze > requirements.txt

# test for s3, dynamodb
test_all_resources:
	python sample_dynamodb.py
	python sample_s3.py
	python sample.py