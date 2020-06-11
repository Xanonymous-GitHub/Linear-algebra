args=("$@")
mkdir hw_0${args[0]}
cp ./*.py ./hw_0${args[0]}
cp ./*.docx ./hw_0${args[0]}
zip -r ./108820003_林天佑.zip ./hw_0${args[0]}/*
mv ./108820003_林天佑.zip ~/Desktop/
rm -rf ./hw_0${args[0]}
