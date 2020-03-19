# This is the latest version!
# This is the latest version!
# This is the latest version!
# This is the latest version!
# This is the latest version!
# This is the latest version!
# This is the latest version!
# This is the latest version!
# This is the latest version!
# This is the latest version!



from time import sleep



play = 1
while(play == 1):
    if play == 1:
        num = 0
        num_set= 0
        pro = 0
        ama = 0
        imput_count = 0
        next = 0
        go = 0
        bre = 0
        bre1 = 0
        cur = 0
        cur1 = 0
        cur2 = 0
        cur3 = 0
        res = 0
        sstop = 0
        End = 0










        print('ルール説明は必要ですか？')
        tut_set = 0
        while(int(tut_set) < 1 or int(tut_set) > 2):
            tut = input('1.必要 2.不必要：')
            tut_set = tut

            if int(tut) == 1:
                    tut_set = 1
                    sleep(0.5)
                    print('========================================')
                    print('1.はじめに負けとなる番号を設定します(番号は30～99で設定してください)')
                    print('2.あなたとコンピューターで交互に、連続した番号を一度に1個～3個まで言います')
                    print('3.初めに設定した番号をいった側の負けです')
                    print('[先攻はあなたです]')
                    print('========================================')
                #========================================
                #はじめに負けとなる番号を設定します
                #負けとなる番号は30～99で設定してください
                #その番号をいった側の負けです
                #番号は交互に、連続して一度に連続して1個～3個まで言うことができます
                #先攻はあなたです
                #========================================
                #[tut_set=1]

                    sleep(0.5)
                    print('例を見ますか？')
                    exa = 0
                    while(exa < 1 or exa >2):
                        inp = input('1.見る 2.見ない：')
                        exa = int(inp)
                        if exa == 1:
                            print('========================================')
                            print('{番号：10}')
                            sleep(0.1)
                            print('[あなた]：[1]...[2]')
                            sleep(0.1)
                            print('[コンピューター]：[3]...[4]...[5]')
                            sleep(0.1)
                            print('[あなた]：[6]')
                            sleep(0.1)
                            print('[コンピューター]：[7]...[8]...[9]')
                            sleep(0.1)
                            print('[あなた]：[10]')
                            sleep(0.1)
                            print('この場合、10をいった、"あなた"の負けです')
                            print('========================================')

                        elif exa == 2:
                            print('========================================')
                            print('例をスキップします')
                            print('========================================')

                        else:
                            continue





            elif int(tut) == 2:
                    tut_set = 2
                    print('========================================')
                    print('説明をスキップします')
                    print('========================================')
                #========================================
                #説明をスキップします
                #========================================
                #[tut_set=2]

            else:
                print('>>>>>必要...1 不必要...2<<<<<')

                if int(tut_set) < 1 or int(tut_set) > 2:
                    continue



        num_set = 0
        while(int(num_set) < 30 or int(num_set) > 99):
            input_count = input('負けとなる番号を設定してください(30～99)：')
            num_set = input_count
            num = input_count
            pro = int(num) - 1
            ama = pro % 4
            next = int(num) - 4
            #[set=0]
            #番号を設定してください
            #[num_set=input_count]
            #[set=inpout]
            #[負け数(number)=input_number]
            #[必勝数(pro)=num-1]
            #[余り(ama)=pro%4]
            #[攻防脱出番号(next)=num-4]

            if int(num_set) < 30 or int(num_set) > 99:
                print('>>>30～99で設定してください<<<')
                continue

        print('番号を' + '[' + str(input_count) + ']' + 'にしました')



        print(str(num) + 'をいった側の負けです')
        print('ゲームを開始します')
        print('========================================')
        sleep(0.5)
        #========================================
        #numberをいった側の負けです
        #ゲームを開始します
        #========================================










        #ama=1
        if ama == 1:
            cur = 0
            bre = 0
            res = 'lose'
            res = 'skip'
            sstop = int(num) - 4
            if ama == 1:
                while(res == 'skip'):
                    while(bre == 0):
                        #プレイヤー
                        print('あなたの番です')
                        cur1 = cur + 1
                        cur2 = cur + 2
                        cur3 = cur + 3
                        print('いくつまで数字を進めますか')
                        print('次の番号は' + str(cur1) + 'からです')
                        #[bre=0]
                        #いくつ数字を進めますか
                        #次の番号は(cur1)です
                        #(cur1)から(cur3)の範囲できめてください:(input)
                        #[go=input]

                        go = input(str(cur1) + 'から' + str(cur3) + 'の範囲できめてください：')
                        #(cur1)から(cur3)の範囲できめてください:(input)
                        go = int(go) - cur

                        if int(go) == 1:
                            print('1進めます')
                            print('[あなた]：' + '[' + str(cur1) + ']')
                            print('========================================')
                            bre = 1
                            cur = cur1
                        elif int(go) == 2:
                            print('2進めます')
                            print('[あなた]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']...' )
                            print('========================================')
                            bre = 2
                            cur = cur2
                        elif int(go) == 3:
                            print('3進めます')
                            print('[あなた]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']...' + '[' + str(cur3) + ']')
                            print('========================================')
                            bre = 3
                            cur = cur3

                        if bre == 0:
                            print('>>>>>' + str(cur1) + 'から' + str(cur3) + 'の範囲できめてください<<<<<')
                            continue


                        #コンピューター
                        sleep(0.5)
                        print('コンピューターの番です')
                        cur1 = cur + 1
                        cur2 = cur + 2
                        cur3 = cur + 3
                        if cur == sstop:
                            print('sstop')
                            res = 'lose'
                        elif cur < int(num):
                            if cur % 4 == 0:
                                cur = cur1
                                #win
                                res = 'win'
                                print('[コンピューター]：' + '[' + str(cur1) + ']')
                                print('========================================')
                            elif cur % 4 == 1:
                                cur = cur1
                                #Back to Back
                                res = 'skip'
                                if cur == sstop:
                                    res = 'lose'
                                else:
                                    print('[コンピューター]：' + '[' + str(cur1) + ']')
                                    print('========================================')
                                    bre = 0
                            elif cur % 4 == 2:
                                cur = cur3
                                #win
                                res = 'win'
                                print('[コンピューター]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']...' + '[' + str(cur3) + ']')
                                print('========================================')
                            elif cur % 4 == 3:
                                cur = cur2
                                #win
                                res = 'win'
                                print('[コンピューター]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']')
                                print('========================================')


                    if res == 'skip':
                        continue





            #2nd turn
            bre = 0
            if ama == 1 and res == 'win':
                while int(cur) < pro:
                    while(bre == 0):
                            #プレイヤー
                            print('あなたの番です')
                            cur1 = cur + 1
                            cur2 = cur + 2
                            cur3 = cur + 3
                            print('いくつまで数字を進めますか')
                            print('次の番号は' + str(cur1) + 'からです')
                            #[bre=0]
                            #いくつ数字を進めますか
                            #次の番号は(cur1)です
                            #(cur1)から(cur3)の範囲できめてください:(input)
                            #[go=input]

                            go = input(str(cur1) + 'から' + str(cur3) + 'の範囲できめてください：')
                            #(cur1)から(cur3)の範囲できめてください:(input)
                            go = int(go) - cur

                            if int(go) == 1:
                                print('1進めます')
                                print('[あなた]：' + '[' + str(cur1) + ']')
                                print('========================================')
                                bre = 1
                                cur = cur1
                            elif int(go) == 2:
                                print('2進めます')
                                print('[あなた]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']' )
                                print('========================================')
                                bre = 2
                                cur = cur2
                            elif int(go) == 3:
                                print('3進めます')
                                print('[あなた]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']...' + '[' + str(cur3) + ']')
                                print('========================================')
                                bre = 3
                                cur = cur3
                            else:
                                bre = 0

                            if bre == 0:
                                print('>>>>>' + str(cur1) + 'から' + str(cur3) + 'の範囲できめてください<<<<<')
                                continue


                    #コンピューター
                    sleep(0.5)
                    print('コンピューターの番です')
                    cur1 = cur + 1
                    cur2 = cur + 2
                    cur3 = cur + 3
                    if bre == 1:
                        cur = cur3
                        #Back to Back
                        print('[コンピューター]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']...' + '[' + str(cur3) + ']')
                        print('========================================')
                    elif bre == 2:
                        cur = cur2
                        #win
                        print('[コンピューター]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']')
                        print('========================================')
                    elif bre == 3:
                        cur = cur1
                        #win
                        print('[コンピューター]：' + '[' + str(cur1) + ']')
                        print('========================================')

                    if int(cur) < pro:
                        bre= 0
                        continue


            #win
            bre = 0
            if res == 'win':
                while(bre == 0):
                    print('あなたの番です')
                    end = input('次は' + str(num) + 'です：')
                    if int(end) == int(num):
                        bre = 1
                    else:
                        bre = 0
                    if bre == 0:
                        continue
                sleep(0.5)
                print('========================================')
                print('あなたの負けです')






            #lose
            bre1 = 0
            if res == 'lose':
                while(bre1 == 0):
                    print('[コンピューター]：' + '[' + str(cur1) + ']')

                    #プレイヤー
                    print('あなたの番です')
                    cur1 = cur + 1
                    cur2 = cur + 2
                    cur3 = cur + 3
                    print('いくつまで数字を進めますか')
                    print('次の番号は' + str(cur1) + 'からです')
                    #[bre=0]
                    #いくつ数字を進めますか
                    #次の番号は(cur1)です
                    #(cur1)から(cur3)の範囲できめてください:(input)
                    #[go=input]

                    go = input(str(cur1) + 'から' + str(cur3) + 'の範囲できめてください：')
                    #(cur1)から(cur3)の範囲できめてください:(input)
                    go = int(go) - cur

                    if go == 1:
                        bre1 = 1
                        print('1進めます')
                        print('[あなた]：' + '[' + str(cur1) + ']')
                        cur = cur + 1

                        cur1 = cur + 1
                        cur2 = cur + 2
                        sleep(0.5)
                        print('========================================')
                        print('[コンピューター]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']' )

                        while(bre == 0):
                            print('あなたの番です')
                            end = input('次は' + str(num) + 'です：')

                            if int(end) == int(num):
                                bre = 1
                            else:
                                bre = 0

                            if bre == 0:
                                continue

                        sleep(0.5)
                        print('========================================')
                        print('あなたの負けです')

                    elif go == 2:
                        bre1 = 2
                        print('2進めます')
                        print('[あなた]：' + '[' + str(cur1) + ']...' + '[' + str(cur1) + ']')
                        cur = cur + 2

                        cur1 = cur + 1
                        sleep(0.5)
                        print('========================================')
                        print('[コンピューター]：' + '[' + str(cur2) + ']' )

                        while(bre == 0):
                            print('あなたの番です')
                            end = input('次は' + str(num) + 'です：')

                            if int(end) == int(num):
                                bre = 1
                            else:
                                bre = 0

                            if bre == 0:
                                continue

                        sleep(0.5)
                        print('========================================')
                        print('あなたの負けです')

                    elif go == 3:
                        bre1 = 3
                        print('3進めます')
                        print('[あなた]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']...' + '[' + str(cur3) + ']')
                        print('========================================')
                        cur = cur + 4
                        sleep(0.5)
                        print('コンピューターの番です')
                        print('[コンピューター]：' + '[' + str(cur) + ']')
                        sleep(0.5)
                        print('========================================')
                        print('あなたの勝ちです')

                    else:
                        bre1 = 0

                        if bre1 == 0:
                            continue











        #ama=2
        if ama == 2:
            cur = 0
            bre = 0
            res = 'lose'
            res = 'skip'
            sstop = int(num) - 1
            if ama == 2:
                while(res == 'skip'):
                    while(bre == 0):
                        #プレイヤー
                        print('あなたの番です')
                        cur1 = cur + 1
                        cur2 = cur + 2
                        cur3 = cur + 3
                        print('いくつまで数字を進めますか')
                        print('次の番号は' + str(cur1) + 'からです')
                        #[bre=0]
                        #いくつ数字を進めますか
                        #次の番号は(cur1)です
                        #(cur1)から(cur3)の範囲できめてください:(input)
                        #[go=input]

                        go = input(str(cur1) + 'から' + str(cur3) + 'の範囲できめてください：')
                        #(cur1)から(cur3)の範囲できめてください:(input)
                        go = int(go) - cur

                        if int(go) == 1:
                            print('1進めます')
                            print('[あなた]：' + '[' + str(cur1) + ']')
                            print('========================================')
                            bre = 1
                            cur = cur1
                        elif int(go) == 2:
                            print('2進めます')
                            print('[あなた]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']...' )
                            print('========================================')
                            bre = 2
                            cur = cur2
                        elif int(go) == 3:
                            print('3進めます')
                            print('[あなた]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']...' + '[' + str(cur3) + ']')
                            print('========================================')
                            bre = 3
                            cur = cur3

                        if bre == 0:
                            print('>>>>>' + str(cur1) + 'から' + str(cur3) + 'の範囲できめてください<<<<<')
                            continue

                        #コンピューター
                        sleep(0.5)
                        print('コンピューターの番です')
                        cur1 = cur + 1
                        cur2 = cur + 2
                        cur3 = cur + 3
                        if cur == sstop:
                            #Exa.31 = 26
                            res = 'lose'
                        elif cur < int(num):
                            if cur == 5:
                                cur = cur1
                                #win
                                res = 'win'
                                print('[コンピューター]：' + '[' + str(cur1) + ']')
                                print('========================================')
                            elif cur % 4 == 0:
                                cur = cur2
                                #win
                                res = 'win'
                                print('[コンピューター]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']')
                            elif cur % 4 == 1:
                                cur = cur1
                                #win
                                res = 'win'
                                print('[コンピューター]：' + '[' + str(cur1) + ']')
                                print('========================================')
                            elif cur % 4 == 2:
                                cur = cur1
                                #Back to Back
                                res = 'skip'
                                if cur == sstop:
                                    res = 'lose'
                                else:
                                    print('[コンピューター]：' + '[' + str(cur1) + ']')
                                    print('========================================')
                                    bre = 0
                            elif cur % 4 == 3:
                                cur = cur3
                                #win
                                res = 'win'
                                print('[コンピューター]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']...' + '[' + str(cur3) + ']')
                                print('========================================')


                                if res == 'skip':
                                    continue



                #2nd turn
                bre = 0
                if ama == 2 and res == 'win':
                    while int(cur) < pro:
                        while(bre == 0):
                                #プレイヤー
                                print('あなたの番です')
                                cur1 = cur + 1
                                cur2 = cur + 2
                                cur3 = cur + 3
                                print('いくつまで数字を進めますか')
                                print('次の番号は' + str(cur1) + 'からです')
                                #[bre=0]
                                #いくつ数字を進めますか
                                #次の番号は(cur1)です
                                #(cur1)から(cur3)の範囲できめてください:(input)
                                #[go=input]

                                go = input(str(cur1) + 'から' + str(cur3) + 'の範囲できめてください：')
                                #(cur1)から(cur3)の範囲できめてください:(input)
                                go = int(go) - cur

                                if int(go) == 1:
                                    print('1進めます')
                                    print('[あなた]：' + '[' + str(cur1) + ']')
                                    print('========================================')
                                    bre = 1
                                    cur = cur1
                                elif int(go) == 2:
                                    print('2進めます')
                                    print('[あなた]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']' )
                                    print('========================================')
                                    bre = 2
                                    cur = cur2
                                elif int(go) == 3:
                                    print('3進めます')
                                    print('[あなた]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']...' + '[' + str(cur3) + ']')
                                    print('========================================')
                                    bre = 3
                                    cur = cur3
                                else:
                                    bre = 0

                                if bre == 0:
                                    print('>>>>>' + str(cur1) + 'から' + str(cur3) + 'の範囲できめてください<<<<<')
                                    continue


                        #コンピューター
                        sleep(0.5)
                        print('コンピューターの番です')
                        cur1 = cur + 1
                        cur2 = cur + 2
                        cur3 = cur + 3
                        if bre == 1:
                            cur = cur3
                            #Back to Back
                            print('[コンピューター]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']...' + '[' + str(cur3) + ']')
                            print('========================================')
                        elif bre == 2:
                            cur = cur2
                            #win
                            print('[コンピューター]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']')
                            print('========================================')
                        elif bre == 3:
                            cur = cur1
                            #win
                            print('[コンピューター]：' + '[' + str(cur1) + ']')
                            print('========================================')

                        if int(cur) < pro:
                            bre= 0
                            continue



                #win
                bre = 0
                if res == 'win':
                    while(bre == 0):
                        print('あなたの番です')
                        end = input('次は' + str(num) + 'です：')
                        if int(end) == int(num):
                            bre = 1
                        else:
                            bre = 0
                        if bre == 0:
                            continue
                    sleep(0.5)
                    print('========================================')
                    print('あなたの負けです')



                #lose
                if res == 'lose':
                    cur = cur + 1
                    sleep(0.5)
                    print('[コンピューター]：' + '[' + str(cur) + ']')
                    sleep(0.5)
                    print('========================================')
                    print('あなたの勝ちです')










        #ama=3
        if ama == 3:
            cur = 0
            bre = 0
            res = 'lose'
            res = 'skip'
            sstop = int(num) - 5
            if ama == 3:
                while(res == 'skip'):
                    while(bre == 0):
                        #プレイヤー
                        print('あなたの番です')
                        cur1 = cur + 1
                        cur2 = cur + 2
                        cur3 = cur + 3
                        print('いくつまで数字を進めますか')
                        print('次の番号は' + str(cur1) + 'からです')
                        #[bre=0]
                        #いくつ数字を進めますか
                        #次の番号は(cur1)です
                        #(cur1)から(cur3)の範囲できめてください:(input)
                        #[go=input]

                        go = input(str(cur1) + 'から' + str(cur3) + 'の範囲できめてください：')
                        #(cur1)から(cur3)の範囲できめてください:(input)
                        go = int(go) - cur

                        if int(go) == 1:
                            print('1進めます')
                            print('[あなた]：' + '[' + str(cur1) + ']')
                            print('========================================')
                            bre = 1
                            cur = cur1
                        elif int(go) == 2:
                            print('2進めます')
                            print('[あなた]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']' )
                            print('========================================')
                            bre = 2
                            cur = cur2
                        elif int(go) == 3:
                            print('3進めます')
                            print('[あなた]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']...' + '[' + str(cur3) + ']')
                            print('========================================')
                            bre = 3
                            cur = cur3

                        if bre == 0:
                            print('>>>>>' + str(cur1) + 'から' + str(cur3) + 'の範囲できめてください<<<<<')
                            continue

                        #コンピューター
                        sleep(0.5)
                        print('コンピューターの番です')
                        cur1 = cur + 1
                        cur2 = cur + 2
                        cur3 = cur + 3
                        if cur == sstop:
                            res = 'lose'
                        elif cur < int(num):
                            if cur == sstop:
                                res = lose
                            if cur == 5:
                                cur = cur2
                                #win
                                res = 'win'
                                print('[コンピューター]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']')
                                print('========================================')
                            elif cur == 5:
                                cur = cur1
                                #win
                                res = 'win'
                                print('[コンピューター]：' + '[' + str(cur1) + ']')
                                print('========================================')
                            elif cur % 4 == 0:
                                cur = cur3
                                #win
                                res = 'win'
                                print('[コンピューター]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']' + '[' + str(cur3) + ']')
                            elif cur % 4 == 1:
                                cur = cur2
                                #win
                                res = 'win'
                                print('[コンピューター]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']')
                            elif cur % 4 == 2:
                                cur = cur1
                                #win
                                res = 'win'
                                print('[コンピューター]：' + '[' + str(cur1) + ']')
                                print('========================================')
                            elif cur % 4 == 3:
                                cur = cur1
                                #Back to Back
                                res = 'skip'
                                print('[コンピューター]：' + '[' + str(cur1) + ']')
                                print('========================================')
                                bre = 0

                            if res == 'skip':
                                continue



            #2nd turn
            bre = 0
            if ama == 3 and res == 'win':
                while int(cur) < pro - 3:
                    while(bre == 0):
                            #プレイヤー
                            print('あなたの番です')
                            cur1 = cur + 1
                            cur2 = cur + 2
                            cur3 = cur + 3
                            print('いくつまで数字を進めますか')
                            print('次の番号は' + str(cur1) + 'からです')
                            #[bre=0]
                            #いくつ数字を進めますか
                            #次の番号は(cur1)です
                            #(cur1)から(cur3)の範囲できめてください:(input)
                            #[go=input]

                            go = input(str(cur1) + 'から' + str(cur3) + 'の範囲できめてください：')
                            #(cur1)から(cur3)の範囲できめてください:(input)
                            go = int(go) - cur

                            if int(go) == 1:
                                print('1進めます')
                                print('[あなた]：' + '[' + str(cur1) + ']')
                                print('========================================')
                                bre = 1
                                cur = cur1
                            elif int(go) == 2:
                                print('2進めます')
                                print('[あなた]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']' )
                                print('========================================')
                                bre = 2
                                cur = cur2
                            elif int(go) == 3:
                                print('3進めます')
                                print('[あなた]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']...' + '[' + str(cur3) + ']')
                                print('========================================')
                                bre = 3
                                cur = cur3
                            else:
                                bre = 0

                            if bre == 0:
                                print('>>>>>' + str(cur1) + 'から' + str(cur3) + 'の範囲できめてください<<<<<')
                                continue


                    #コンピューター
                    sleep(0.5)
                    print('コンピューターの番です')
                    cur1 = cur + 1
                    cur2 = cur + 2
                    cur3 = cur + 3
                    if bre == 1:
                        cur = cur3
                        #Back to Back
                        print('[コンピューター]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']...' + '[' + str(cur3) + ']')
                        print('========================================')
                    elif bre == 2:
                        cur = cur2
                        #win
                        print('[コンピューター]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']')
                        print('========================================')
                    elif bre == 3:
                        cur = cur1
                        #win
                        print('[コンピューター]：' + '[' + str(cur1) + ']')
                        print('========================================')

                    if int(cur) < pro:
                        bre= 0
                        continue



            #lose
            if res == 'lose':
                cur = cur + 1
                sleep(0.5)
                print('[コンピューター]：' + '[' + str(cur) + ']')
                print('========================================')
                while(bre == 0):
                        #プレイヤー
                        print('あなたの番です')
                        cur1 = cur + 1
                        cur2 = cur + 2
                        cur3 = cur + 3
                        print('いくつまで数字を進めますか')
                        print('次の番号は' + str(cur1) + 'からです')
                        #[bre=0]
                        #いくつ数字を進めますか
                        #次の番号は(cur1)です
                        #(cur1)から(cur3)の範囲できめてください:(input)
                        #[go=input]

                        go = input(str(cur1) + 'から' + str(cur3) + 'の範囲できめてください：')
                        #(cur1)から(cur3)の範囲できめてください:(input)
                        go = int(go) - cur

                        if int(go) == 1:
                            print('1進めます')
                            print('[あなた]：' + '[' + str(cur1) + ']')
                            print('========================================')
                            bre = 1
                            cur = cur1
                        elif int(go) == 2:
                            print('2進めます')
                            print('[あなた]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']' )
                            print('========================================')
                            bre = 2
                            cur = cur2
                        elif int(go) == 3:
                            print('3進めます')
                            print('[あなた]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']...' + '[' + str(cur3) + ']')
                            print('========================================')
                            bre = 3
                            cur = cur3
                        else:
                            bre = 0

                        if bre == 0:
                            print('>>>>>' + str(cur1) + 'から' + str(cur3) + 'の範囲できめてください<<<<<')
                            continue

                #コンピューター
                sleep(0.5)
                print('コンピューターの番です')
                cur1 = cur + 1
                cur2 = cur + 2
                cur3 = cur + 3
                if bre == 1:
                    cur = cur2
                    #win
                    print('[コンピューター]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']')
                    print('========================================')
                    res = 'win'
                elif bre == 2:
                    cur = cur1
                    #win
                    print('[コンピューター]：' + '[' + str(cur1) + ']')
                    res = 'win'
                elif bre == 3:
                    print('[コンピューター]：' + '[' + str(cur1) + ']')
                    res = 'lose'
                    sleep(0.5)
                    print('========================================')
                    print('あなたの勝ちです')



            #win
            bre = 0
            if res == 'win':
                while(bre == 0):
                    print('あなたの番です')
                    end = input('次は' + str(num) + 'です：')
                    if int(end) == int(num):
                        bre = 1
                    else:
                        bre = 0
                    if bre == 0:
                        continue
                sleep(0.5)
                print('========================================')
                print('あなたの負けです')










        #ama=4
        if ama == 0:
            turn = 1
            if ama == 0:
                cur = 0
                bre = 0
                res = 'lose'
                res = 'skip'
                sstop = int(num) - 3
                if ama == 0:
                    while(cur < int(num) - 4):
                        while(bre == 0):
                            #プレイヤー
                            print('あなたの番です')
                            cur1 = cur + 1
                            cur2 = cur + 2
                            cur3 = cur + 3
                            print('いくつまで数字を進めますか')
                            print('次の番号は' + str(cur1) + 'からです')
                            #[bre=0]
                            #いくつ数字を進めますか
                            #次の番号は(cur1)です
                            #(cur1)から(cur3)の範囲できめてください:(input)
                            #[go=input]

                            go = input(str(cur1) + 'から' + str(cur3) + 'の範囲できめてください：')
                            #(cur1)から(cur3)の範囲できめてください:(input)
                            go = int(go) - cur

                            if int(go) == 1:
                                print('1進めます')
                                print('[あなた]：' + '[' + str(cur1) + ']')
                                print('========================================')
                                bre = 1
                                cur = cur1
                            elif int(go) == 2:
                                print('2進めます')
                                print('[あなた]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']...' )
                                print('========================================')
                                bre = 2
                                cur = cur2
                            elif int(go) == 3:
                                print('3進めます')
                                print('[あなた]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']...' + '[' + str(cur3) + ']')
                                print('========================================')
                                bre = 3
                                cur = cur3

                            if bre == 0:
                                print('>>>>>' + str(cur1) + 'から' + str(cur3) + 'の範囲できめてください<<<<<')
                                continue



                        #コンピューター
                        sleep(0.5)
                        print('コンピューターの番です')
                        cur1 = cur + 1
                        cur2 = cur + 2
                        cur3 = cur + 3
                        if turn == 1:
                            if cur % 4 == 1:
                                cur = cur3
                                #win(skip)
                                print('[コンピューター]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']...' + '[' + str(cur3) + ']')
                                print('========================================')
                                res = 'skip'
                                turn = 2
                                bre = 0

                            elif cur % 4 == 2:
                                cur = cur2
                                #win(skip)
                                print('[コンピューター]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']')
                                print('========================================')
                                res = 'skip'
                                turn = 2
                                bre = 0
                            elif cur % 4 == 3:
                                cur = cur1
                                #win(skip)
                                print('[コンピューター]：' + '[' + str(cur1) + ']')
                                print('========================================')
                                res = 'skip'
                                turn = 2
                                bre = 0

                        if turn == 2:
                            if cur == sstop:
                                print('sstop')
                                res = 'win'
                            elif cur == int(num) - 4:
                                break
                            elif cur == int(num) - 3:
                                break
                            elif cur == int(num) - 2:
                                break
                            elif cur < int(num) - 4:
                                curr = cur % 4

                                if cur % 4 == 1:
                                    cur = cur3
                                    #win(skip)
                                    print('[コンピューター]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']...' + '[' + str(cur3) + ']')
                                    print('========================================')
                                    res = 'skip'
                                    bre = 0
                                elif cur % 4 == 2:
                                    cur = cur2
                                    #win(skip)
                                    print('[コンピューター]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']')
                                    print('========================================')
                                    res = 'skip'
                                    bre = 0
                                elif cur % 4 == 3:
                                    cur = cur1
                                    #win(skip)
                                    print('[コンピューター]：' + '[' + str(cur1) + ']')
                                    print('========================================')
                                    res = 'skip'
                                    bre = 0

                                if cur < pro or res == 'skip':
                                    continue



            if cur == int(num) - 4:
                print('[コンピューター]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']...' + '[' + str(cur3) + ']')
                print('========================================')
            if cur == int(num) - 3:
                print('[コンピューター]：' + '[' + str(cur1) + ']...' + '[' + str(cur2) + ']')
                print('========================================')
            if cur == int(num) - 2:
                print('[コンピューター]：' + '[' + str(cur1) + ']')
                print('========================================')



            bre = 0
            while(bre == 0):
                print('あなたの番です')
                end = input('次は' + str(num) + 'です：')
                if int(end) == int(num):
                    bre = int(num) - cur
                else:
                    bre = 0
                if bre == 0:
                    continue

            sleep(0.5)
            print('========================================')
            print('あなたの負けです')




        print('========================================')
        print('もういちどやりますか？')
        bre1 = 0
        while(bre1 == 0):
            sleep(0.5)
            bre1 = input('はい...1 いいえ...2：')
            if  int(bre1) == 1:
                bre1 = 1
                play = bre1
            elif int(bre1) == 2:
                bre1 = 2
                play = bre1
            else:
                continue


            if bre1 == 1:
                sleep(0.5)
                print('もう一回！')
                print('========================================')
                print('========================================')
                print('========================================')
                sleep(1)
                play = 1
            elif bre1 ==2:
                sleep(0.5)
                print('ゲームを終了します')
                print('========================================')
                print('========================================')
                print('========================================')
                quit()










        continue
