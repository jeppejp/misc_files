#include <memory>
#include <cppunit/extensions/TestFactoryRegistry.h>
#include <cppunit/ui/text/TestRunner.h>
#include <cppunit/CompilerOutputter.h>
#include <cppunit/TestCase.h>
#include <cppunit/extensions/HelperMacros.h>

#include "Filereader.hpp"

class FileReaderTestCase : public CppUnit::TestCase
{


    CPPUNIT_TEST_SUITE( FileReaderTestCase );
    CPPUNIT_TEST( filenotfound );
    CPPUNIT_TEST( filefound );
    CPPUNIT_TEST_SUITE_END();


    double          m_value1;
    double          m_value2;
    void            filenotfound ();
    void            filefound();

    public:


    void            setUp ();
};




CPPUNIT_TEST_SUITE_NAMED_REGISTRATION( FileReaderTestCase, "FileReaderTestCase" );


void FileReaderTestCase::setUp ()
{
    m_value1 = 2.0;
    m_value2 = 3.0;
}



void FileReaderTestCase::filenotfound ()
{
    Filereader fr("somefile.notfound");
    CPPUNIT_ASSERT_EQUAL(false, fr.readFile());
}

void FileReaderTestCase::filefound()
{
    Filereader fr("100points.txt");
    CPPUNIT_ASSERT_EQUAL(true, fr.readFile());
}




CppUnit::Test *suite()
{
    CppUnit::TestFactoryRegistry &registry =
        CppUnit::TestFactoryRegistry::getRegistry();


    registry.registerFactory(
            &CppUnit::TestFactoryRegistry::getRegistry( "FileReaderTestCase" ) );
    return registry.makeTest();
}



int main( int argc, char* argv[] )
{
    bool selfTest = (argc > 1)  && (std::string("-selftest") == argv[1]);
    CppUnit::TextUi::TestRunner runner;
    runner.addTest( suite() );   // Add the top suite to the test runner
    if ( selfTest )
    { // Change the default outputter to a compiler error format outputter
        runner.setOutputter( CppUnit::CompilerOutputter::defaultOutputter(
        &runner.result(),
        std::cerr ) );
    }
    bool wasSucessful = runner.run( "" );
    return wasSucessful ? 0 : 1;
}
