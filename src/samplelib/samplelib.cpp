#include <iostream>
#include <fstream>
#include <Python.h>

class SampleObject {
  public:
    SampleObject() {
      std::cout << "Instance created" << std::endl;
    }

    ~SampleObject() {
      std::cout << "Instance teardown" << std::endl; 
    }

    void echo(const char* str){
      std::cout << str << std::endl;
    }

    void doHello(){
      std::cout << "Hello" << std::endl;
    }
};

extern "C" {

  SampleObject* newSampleObject() {
    return new SampleObject();
  }

  void delSampleObject(SampleObject* obj){
    delete obj;
  }

  void callEcho(SampleObject* obj, const char* str) {
    obj->echo(str);
  }

  void callDoHello(SampleObject* obj){
    obj->doHello();
  }

  char* callRead(SampleObject* obj, const char* file) {
    std::ifstream ifs(file, std::ifstream::in);
    std::string contents((std::istreambuf_iterator<char>(ifs)), std::istreambuf_iterator<char>());

    char *cstr = new char[contents.length() + 1];
    strcpy(cstr, contents.c_str());

    return cstr;
  }

}
