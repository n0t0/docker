sed -e s/_test_1/_test_i/g -e s/test_2/test_ii/g < test.txt > /shared/test.txt
sed -e s/_test_1/_test_i/g -e s/test_2/test_ii/g < test.txt > test.txt

echo "current directory"
ls .

echo "/app"
ls /app

echo "/shared"
ls /shared

