# coding: utf-8

"""
__title__ = 'format_jupyter_py'
__author__ = 'Jeffmxh'

                   _ooOoo_
                  o8888888o
                  88" . "88
                  (| -_- |)
                  O\  =  /O
               ____/`---'\____
             .'  \\|     |//  `.
            /  \\|||  :  |||//  \
           /  _||||| -:- |||||-  \
           |   | \\\  -  /// |   |
           | \_|  ''\---/''  |   |
           \  .-\__  `-`  ___/-. /
         ___`. .'  /--.--\  `. . __
      ."" '<  `.___\_<|>_/___.'  >'"".
     | | :  `- \`.;`\ _ /`;.`/ - ` : | |
     \  \ `-.   \_ __\ /__ _/   .-` /  /
======`-.____`-.___\_____/___.-`____.-'======
                   `=---='
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            佛祖保佑       永无BUG
"""

import argparse
import re

class ScriptFormatter:
    '''用于将从jupyter保存的py文件格式化，自动添加佛祖！
    '''
    author = 'Jeffmxh'
    my_title = r'''
# coding: utf-8

"""
__title__ = '{}'
__author__ = '{}'

                   _ooOoo_
                  o8888888o
                  88" . "88
                  (| -_- |)
                  O\  =  /O
               ____/`---'\____
             .'  \\|     |//  `.
            /  \\|||  :  |||//  \
           /  _||||| -:- |||||-  \
           |   | \\\  -  /// |   |
           | \_|  ''\---/''  |   |
           \  .-\__  `-`  ___/-. /
         ___`. .'  /--.--\  `. . __
      ."" '<  `.___\_<|>_/___.'  >'"".
     | | :  `- \`.;`\ _ /`;.`/ - ` : | |
     \  \ `-.   \_ __\ /__ _/   .-` /  /
======`-.____`-.___\_____/___.-`____.-'======
                   `=---='
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            佛祖保佑       永无BUG
"""
    '''.strip() + '\n'
    def __init__(self):
        pass

    @staticmethod
    def classify_script(raw_script, file_name='my_awesome_code'):
        '''
        主函数，将代码进行分类，然后分别格式化，最终构建输出
        '''
        assert isinstance(raw_script, list)
        import_statements = []
        from_import_statements = []
        class_statements = []
        func_statements = []
        main_func_statements = []
        IS_CLASS_INNER = False
        IS_FUNC_INNER = False
        line_cache = ''
        temp = [x for x in raw_script if not \
                re.search(r'/usr/bin/|coding: utf-8|In\[(\d|\s)+\]', x)]
        temp = [re.sub(r'^\s+?\n', '\n', x) for x in temp]
        while temp:
            line = temp.pop(0)
            if not IS_CLASS_INNER and not IS_FUNC_INNER:
                if re.match(r'import\s.+?\n', line):
                    import_statements.append(line)
                elif re.match(r'from\s.+?import\s.+?\n', line):
                    from_import_statements.append(line)
                elif re.match(r'^class\s.+?\n', line):
                    line_cache += line
                    IS_CLASS_INNER = True
                elif re.match(r'^def\s.+?\n|^@.+?\n', line):
                    line_cache += line
                    IS_FUNC_INNER = True
                else:
                    main_func_statements.append(line)
            elif IS_CLASS_INNER:
                if re.search(r'^\S', line):
                    IS_CLASS_INNER = False
                    class_statements.append(line_cache)
                    line_cache = ''
                    temp.insert(0, line)
                else:
                    line_cache += line
            elif IS_FUNC_INNER:
                if re.search(r'^\S', line):
                    IS_FUNC_INNER = False
                    func_statements.append(line_cache)
                    line_cache = ''
                    temp.insert(0, line)
                else:
                    line_cache += line
            else:
                pass
        if line_cache:
            if IS_CLASS_INNER:
                class_statements.append(line_cache)
            elif IS_FUNC_INNER:
                func_statements.append(line_cache)
            else:
                pass

        import_statements = ScriptFormatter.format_import(import_statements)
        from_import_statements = ScriptFormatter.format_from_import(from_import_statements)
        class_statements = ScriptFormatter.format_class(class_statements)
        func_statements = ScriptFormatter.format_func(func_statements)
        main_func_statements = ScriptFormatter.format_main(main_func_statements)

        result = ScriptFormatter.my_title.format(file_name, ScriptFormatter.author) + '\n'
        result = result + import_statements if import_statements else result
        result = result + from_import_statements if from_import_statements else result
        result = result + class_statements if class_statements else result
        result = result + func_statements if func_statements else result
        result += main_func_statements if main_func_statements else result
        return re.sub('\n+$', '\n', result)

    @staticmethod
    def format_import(import_statements):
        '''
        将import语句格式化
        '''
        import_statements = sorted(import_statements, key=lambda x: x[7])
        import_statements = ''.join(import_statements) + '\n' if import_statements else ''
        return import_statements

    @staticmethod
    def format_from_import(from_import_statements):
        '''
        将 from xxx import xxx语句格式化
        '''
        from_import_statements = sorted(from_import_statements, key=lambda x: x[5])
        from_import_statements = ''.join(from_import_statements) + '\n\n' \
            if from_import_statements else ''
        return from_import_statements

    @staticmethod
    def format_class(class_statements):
        '''
        将定义类的代码块格式化
        '''
        class_states = [re.sub(r'\n{2,}', '\n\n', x) for x in class_statements]
        class_states = [re.sub(r'\n+$', '\n', x) for x in class_states]
        class_states = '\n\n'.join(class_states) + '\n\n' if class_states else ''
        return class_states

    @staticmethod
    def format_func(func_statements):
        '''
        将定义函数的代码块格式化
        '''
        func_states = [re.sub(r'\n+$', '\n', x) for x in func_statements]
        func_states = '\n'.join(func_states) + '\n' if func_states else ''
        return func_states

    @staticmethod
    def format_main(main_func_statements):
        '''
        将import语句，类，函数定义以外的所有语句放入main之中
        '''
        main_func_statements = [x for x in main_func_statements if not re.search('^\s+$', x)]
        main_func_statements = ['    '+x for x in main_func_statements]
        header = "if __name__ == '__main__':\n"
        main_func_statements.insert(0, header)
        return ''.join(main_func_statements)

def main(input_file, file_title):
    '''
    处理文件主函数
    '''
    assert input_file.endswith('.py')
    raw_script = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            raw_script.append(line)

    format_script = ScriptFormatter.classify_script(raw_script, file_title)
    file_name = re.sub(r'\.py', '', input_file) + '_formated.py'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(format_script)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Jupyter保存python程序格式化脚本')
    parser.add_argument('-f', '--file', dest='input_file', nargs='?', default='',
                        help='Name of the input excel file in folder:raw_data.')
    parser.add_argument('-t', '--title', dest='file_title', nargs='?', default='',
                        help='Name of the input excel file in folder:raw_data.')
    args = parser.parse_args()
    main(args.input_file, args.file_title)
