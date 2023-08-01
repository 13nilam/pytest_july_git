import pytest
class Test_addition_001:
    #user defined marker 'operational'.for same type of testcases we define marker
    #syntax for user defined marker is
    #@pytest.mark.markername
      def test_add_001(self):
        a=10
        b=20
        sum=a+b
        print("sum=a+b",sum)
        if sum == 30:
            print("sum matched")
            assert True
        else:
            print("sum not matched")
            assert False


      def test_mul_002(self):
        a = 10
        b = 20
        mul = a * b
        print("Mul=a+b", mul)
        if mul == 200:
            print("sum matched")
            assert True
        else:
            print("sum not matched")
            assert False
