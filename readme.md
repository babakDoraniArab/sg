how to use it . 

by the way you need to change your region in the python code first . default is eu-west-2

```sh
python aws-get-sg.py --profile STAGE

```

run this command to make it executalbe from anywhere 
```sh

sudo cp aws-get-sg.py /usr/local/bin/aws-get-sg
sudo chmod +x /usr/local/bin/aws-get-sg

```

now you can use it like this 
```sh
aws-get-sg --profile DEV
```
