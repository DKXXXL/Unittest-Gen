# Unittest Generator


def gen(funcName, fileName, inputGeneratorfileName, SMALL_TEST=1, BIG_TEST=1):
    head = ['import unittest',
            'import {} as test1'.format(fileName),
            'import compare.{} as test2'.format(fileName),
            'import {} as igen'.format(inputGeneratorfileName)]
    constantBody =[
        'SMALL_TEST={}'.format(SMALL_TEST),
        'BIG_TEST={}'.format(BIG_TEST)
    ]

    classbody = [
        "_test_{} = lambda x: ([((lambda expIn: x.assertEqual(test1.{}(*expIn),test2.{}(*expIn),expIn))({})) for i in range(SMALL_TEST)])".format(
            funcname, funcname,funcname,
            'igen.gen_{}()'.format(funcname)
        )
        for funcname in funcName
    ]
    classdeclaration = [
        "test_{} = type('class_{}', (unittest.TestCase,), {})".format(
            fileName, fileName, '{' +
            ','.join([
                '"test_{}":_test_{}'.format(funcname, funcname)
                for funcname in funcName

            ]) + '}'
                                                                  )

    ]
    main_body =[
        "[(print('TestCase',i),unittest.main(exit=False)) for i in range(BIG_TEST)]"
    ]
    wholeFile = head + constantBody + classbody + classdeclaration + main_body
    wholeTest = '\n'.join(wholeFile)
    return wholeTest

def main():
    funcName = ['build_tree', 'draw_formula_tree','evaluate','play2win']
    fileName = 'formula_game_functions'
    genfile = 'unittestA2_generator'
    unittestfile = 'Unittest_{}.py'.format(fileName)
    import sys
    (a, sys.stdout) = (sys.stdout, open(unittestfile,'w'))
    print(gen(funcName,fileName,genfile))
    (sys.stdout, a) = (a, sys.stdout)
    a.close()

main()
