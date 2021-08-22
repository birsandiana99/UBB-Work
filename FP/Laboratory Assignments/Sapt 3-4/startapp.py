'''

MAIN FUNCTION

'''
    
def start():
    transList=[]
    set_up(transList)
    commands={"add":add_ui,"remove":remove_ui,"list":list_ui}
    ok=1
    undoList = []
    print("Type <help> for a list of the possible commands")
    while ok:
        user_input=readCommand()
        if user_input[0]=='exit':
            #print(transList)
            return
            ok=0
        elif user_input[0]=='help' and user_input[1]==[]:
            printMenu()
        elif user_input[0]=='add':
            add_ui(transList,user_input[1],undoList)
            
        elif user_input[0]=='insert':
            insert_ui(transList,user_input[1],undoList)
            
        elif user_input[0]=='remove':
            remove_ui(transList,user_input[1],undoList)
            
        elif user_input[0]=='replace':
            replace_ui(transList,user_input[1],undoList)
            
        elif user_input[0]=='list':
            list_ui(transList,user_input[1])

        elif user_input[0]=='sum':
            sum_ui(transList,user_input[1])

        elif user_input[0]=='max':
            max_ui(transList,user_input[1])
        elif user_input[0]=='filter':
            filter_ui(transList,user_input[1],undoList)
        elif user_input[0]=='undo':
            if user_input[1]!=[]:
                print("Invalid command")
            else:
                undo(transList,undoList)
            
        else:
            print("Invalid command")

start()
