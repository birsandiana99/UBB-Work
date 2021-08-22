package View;

import Controller.Controller;
import Model.Expression.*;
import Model.Expression.HeapExpressions.ReadHeapExp;
import Model.ProgramState.*;
import Model.Statements.*;
import Model.Statements.HeapStatements.NewStmt;
import Model.Statements.HeapStatements.WriteHeapStmt;
import Model.Type.BoolType;
import Model.Type.IntType;
import Model.Type.RefType;
import Model.Type.StringType;
import Model.Value.BoolValue;
import Model.Value.IntValue;
import Model.Value.StringValue;
import Model.Value.Value;
import Repository.*;

import java.util.ArrayList;
import java.util.Arrays;

public class Interpreter {
    private static IStmt concatStatements(IStmt... statements) {
        if (statements.length == 1)
            return statements[0];

        return new CompStmt(statements[0], concatStatements(Arrays.copyOfRange(statements, 1, statements.length)));
    }

    public static ArrayList<IStmt> getAllExamples(){
        IStmt ex1= new CompStmt(new VarDeclStmt("v",new IntType()),
                new CompStmt(new AssignStmt("v",new ValueExp(new IntValue(2))), new PrintStmt(new
                        VarExp("v"))));

        IStmt ex2 = new CompStmt( new VarDeclStmt("a",new IntType()),
                new CompStmt(new VarDeclStmt("b",new IntType()),
                        new CompStmt(new AssignStmt("a", new ArithExp('+',new ValueExp(new IntValue(2)),new
                                ArithExp('*',new ValueExp(new IntValue(3)), new ValueExp(new IntValue(5))))),
                                new CompStmt(new AssignStmt("b",new ArithExp('+',new VarExp("a"), new
                                        ValueExp(new IntValue(1)))), new PrintStmt(new VarExp("b"))))));
        IStmt ex3 = new CompStmt(new VarDeclStmt("a",new BoolType()),
                new CompStmt(new VarDeclStmt("v", new IntType()),
                        new CompStmt(new AssignStmt("a", new ValueExp(new BoolValue(true))),
                                new CompStmt(new IfStmt(new VarExp("a"),new AssignStmt("v",new ValueExp(new
                                        IntValue(2))), new AssignStmt("v", new ValueExp(new IntValue(3)))), new PrintStmt(new
                                        VarExp("v"))))));

        IStmt ex4 = new CompStmt(new VarDeclStmt("varf",new StringType()),
                new CompStmt(new AssignStmt("varf",new ValueExp(new StringValue("test.in"))),
                        new CompStmt(new VarDeclStmt("varc",new IntType()),
                                new CompStmt(new openRFileStmt(new VarExp("varf")),
                                        new CompStmt(new readFileStmt(new VarExp("varf"),"varc"),
                                                new CompStmt( new PrintStmt(new VarExp("varc")),
                                                        new CompStmt(new readFileStmt(new VarExp("varf"),"varc"),
                                                                new CompStmt(new PrintStmt(new VarExp("varc")),new closeRFileStmt(new VarExp("varf"))))))))));

        IStmt ex5 = new CompStmt(new VarDeclStmt("s",new StringType()),
                new CompStmt(new AssignStmt("s",new ValueExp(new StringValue("ana"))),new PrintStmt(new VarExp("s"))));


        IStmt ex6 =  new CompStmt(new VarDeclStmt("a",new IntType()),new CompStmt(new NopStmt(),new CompStmt(
                new VarDeclStmt("b",new BoolType()), new CompStmt( new AssignStmt("b",new ValueExp(new BoolValue(true))),
                new CompStmt(new IfStmt(new VarExp("b"),new CompStmt(new AssignStmt("a",new ValueExp(new IntValue(10))),new AssignStmt("b",new ValueExp(new BoolValue(false)))),
                        new CompStmt(new AssignStmt("a",new ValueExp(new IntValue(-10))),new AssignStmt("b",new ValueExp(new BoolValue(false))))),
                        new CompStmt(new PrintStmt(new VarExp("a")),new PrintStmt(new VarExp("b"))))))));


        IStmt ex7 = new CompStmt(new VarDeclStmt("a",new BoolType()),
                new CompStmt(new VarDeclStmt("v", new IntType()),
                        new CompStmt(new AssignStmt("a", new ValueExp(new BoolValue(true))),
                                new CompStmt(new IfStmt(new RelExp(new VarExp("v"),new ValueExp(new IntValue(1)),">"),new AssignStmt("v",new ValueExp(new
                                        IntValue(2))), new AssignStmt("v", new ValueExp(new IntValue(3)))), new PrintStmt(new
                                        VarExp("v"))))));

        IStmt ex8 = new CompStmt(new VarDeclStmt("v",new IntType()),
                new CompStmt(new AssignStmt("v",new ValueExp(new IntValue(4))),
                        new CompStmt(new WhileStmt(new RelExp(new VarExp("v"),new ValueExp(new IntValue(0)),">"),
                                new CompStmt(new PrintStmt(new VarExp("v")),new AssignStmt("v",new ArithExp('-',new VarExp("v"),new ValueExp(new IntValue(1)))))),
                                new PrintStmt(new VarExp("v")))));

        IStmt ex9 = new CompStmt(new VarDeclStmt("v",new RefType(new IntType())),
                new CompStmt(new NewStmt("v",new ValueExp(new IntValue(20))),
                        new CompStmt(new VarDeclStmt("a",new RefType(new RefType(new IntType()))),
                                new CompStmt(new NopStmt(),new CompStmt(
                                        new NewStmt("v",new ValueExp(new IntValue(30))),
                                        new PrintStmt(new ReadHeapExp(new ReadHeapExp(new VarExp("a"))))
                                )))));

        PrgState prg9 = new PrgState(new MyStack<>(), new MyDictionary<>(), new MyList<>(),new MyDictionary<>(), new MyHeap<>(), ex9);

        IStmt ex10 = new CompStmt(new VarDeclStmt("v",new RefType(new IntType())),
                new CompStmt(new NewStmt("v",new ValueExp(new IntValue(20))),
                        new CompStmt(new PrintStmt(new ReadHeapExp(new VarExp("v"))),
                                new CompStmt(new NewStmt("v",new ValueExp(new IntValue(40))),new PrintStmt(new ReadHeapExp(new VarExp("v")))))));

        IStmt ex11 =  new CompStmt(new VarDeclStmt("v",new RefType(new IntType())),
                new CompStmt(new NewStmt("v",new ValueExp(new IntValue(20))),
                        new CompStmt(new VarDeclStmt("a",new RefType(new RefType(new IntType()))),
                                new CompStmt(new NewStmt("a",new VarExp("v")),new CompStmt(new PrintStmt(new ReadHeapExp(new VarExp("v"))),
                                        new PrintStmt(new ArithExp('+',new ReadHeapExp(new ReadHeapExp(new VarExp("a"))),new ValueExp(new IntValue(5)))))))));

        IStmt ex12 = new CompStmt(new VarDeclStmt("v",new RefType(new IntType())),
                new CompStmt(new NewStmt("v",new ValueExp(new IntValue(20))),
                        new CompStmt(new WriteHeapStmt("v",new ValueExp(new IntValue(30))),
                                new PrintStmt(new ArithExp('+',new ReadHeapExp(new VarExp("v")),new ValueExp(new IntValue(5)))))));

        IStmt ex13 = new CompStmt(new VarDeclStmt("v",new IntType()),
                new CompStmt(new AssignStmt("v",new ValueExp(new IntValue(4))),
                        new CompStmt(new WhileStmt(new ArithExp('+',new VarExp("v"),new ValueExp(new IntValue(0))),
                                new CompStmt(new PrintStmt(new VarExp("v")),new AssignStmt("v",new ArithExp('-',new VarExp("v"),new ValueExp(new IntValue(1)))))),
                                new PrintStmt(new VarExp("v")))));

        IStmt ex14 = new CompStmt(new VarDeclStmt("v",new IntType()),new CompStmt(new VarDeclStmt("a",new RefType(new IntType())),
                new CompStmt(new AssignStmt("v",new ValueExp(new IntValue(10))),new CompStmt(new NewStmt("a",new ValueExp(new IntValue(22))),
                        new CompStmt(new ForkStmt(new CompStmt(new WriteHeapStmt("a",new ValueExp(new IntValue(30))),
                                new CompStmt(new AssignStmt("v",new ValueExp(new IntValue(32))), new CompStmt(new PrintStmt(new VarExp("v")),new PrintStmt(new ReadHeapExp(new VarExp("a"))))))),
                                new CompStmt(new PrintStmt(new VarExp("v")),new PrintStmt(new ReadHeapExp(new VarExp("a")))))))));

        IStmt ex15 = new CompStmt(new VarDeclStmt("a",new IntType()),new ForkStmt(new PrintStmt(new VarExp("s"))));

        IStmt ex16 = new CompStmt(new VarDeclStmt("a",new IntType()), new CompStmt(new VarDeclStmt("b",new IntType()),
                new CompStmt(new ForkStmt(new ForkStmt(new PrintStmt(new VarExp("a")))), new ForkStmt(new PrintStmt(new VarExp("b"))))));

        //int a
        //int b
        //int c
        //fork(fork(print a))
        //fork(print b)
        //print c
        IStmt ex17  = new CompStmt(new VarDeclStmt("a", new IntType()), new CompStmt( new VarDeclStmt("b",new IntType()),
                new CompStmt(new VarDeclStmt("c",new IntType()), new CompStmt(new ForkStmt(new ForkStmt(new PrintStmt(new VarExp("a")))),
                        new CompStmt(new ForkStmt(new PrintStmt(new VarExp("b"))), new PrintStmt(new VarExp("c")))))));

        //string s; s=ana; print(a);   => typecheck err
        IStmt ex18 = new CompStmt(new VarDeclStmt("s",new StringType()),
                new CompStmt(new AssignStmt("s",new ValueExp(new StringValue("ana"))),new PrintStmt(new VarExp("a"))));

        //typecheck err ->openRFileStmt(new VarExp("varc")
        IStmt ex19 = new CompStmt(new VarDeclStmt("varf",new StringType()),
                new CompStmt(new AssignStmt("varf",new ValueExp(new StringValue("test.in"))),
                        new CompStmt(new VarDeclStmt("varc",new IntType()),
                                new CompStmt(new openRFileStmt(new VarExp("varc")),
                                        new CompStmt(new readFileStmt(new VarExp("varf"),"varc"),
                                                new CompStmt( new PrintStmt(new VarExp("varc")),
                                                        new CompStmt(new readFileStmt(new VarExp("varf"),"varc"),
                                                                new CompStmt(new PrintStmt(new VarExp("varc")),new closeRFileStmt(new VarExp("varf"))))))))));

        //typecheck err -> closeRFileStmt(new VarExp("varc")
        IStmt ex20 = new CompStmt(new VarDeclStmt("varf",new StringType()),
                new CompStmt(new AssignStmt("varf",new ValueExp(new StringValue("test.in"))),
                        new CompStmt(new VarDeclStmt("varc",new IntType()),
                                new CompStmt(new openRFileStmt(new VarExp("varf")),
                                        new CompStmt(new readFileStmt(new VarExp("varf"),"varc"),
                                                new CompStmt( new PrintStmt(new VarExp("varc")),
                                                        new CompStmt(new readFileStmt(new VarExp("varf"),"varc"),
                                                                new CompStmt(new PrintStmt(new VarExp("varc")),new closeRFileStmt(new VarExp("varc"))))))))));

        //string s; s=1; print(s);   => typecheck err
        IStmt ex21 = new CompStmt(new VarDeclStmt("s",new StringType()),
                new CompStmt(new AssignStmt("s",new ValueExp(new IntValue(1))),new PrintStmt(new VarExp("s"))));

        /*
        int a;
        nop;
        bool b;
        b=true;
        if(a) THEN (a=10;b=false) ELSE (a=-10;b=true;)
        print(a);
        print(b);
         */
        //typecheck err  -> if(a)
        IStmt ex22 =  new CompStmt(new VarDeclStmt("a",new IntType()),new CompStmt(new NopStmt(),new CompStmt(
                new VarDeclStmt("b",new BoolType()), new CompStmt( new AssignStmt("b",new ValueExp(new BoolValue(true))),
                new CompStmt(new IfStmt(new VarExp("a"),new CompStmt(new AssignStmt("a",new ValueExp(new IntValue(10))),new AssignStmt("b",new ValueExp(new BoolValue(false)))),
                        new CompStmt(new AssignStmt("a",new ValueExp(new IntValue(-10))),new AssignStmt("b",new ValueExp(new BoolValue(false))))),
                        new CompStmt(new PrintStmt(new VarExp("a")),new PrintStmt(new VarExp("b"))))))));

        //tyepcheck err -> readFileStmt(new VarExp("varf"),"varf")
        IStmt ex23 = new CompStmt(new VarDeclStmt("varf",new StringType()),
                new CompStmt(new AssignStmt("varf",new ValueExp(new StringValue("test.in"))),
                        new CompStmt(new VarDeclStmt("varc",new IntType()),
                                new CompStmt(new openRFileStmt(new VarExp("varf")),
                                        new CompStmt(new readFileStmt(new VarExp("varf"),"varf"),
                                                new CompStmt( new PrintStmt(new VarExp("varc")),
                                                        new CompStmt(new readFileStmt(new VarExp("varf"),"varc"),
                                                                new CompStmt(new PrintStmt(new VarExp("varc")),new closeRFileStmt(new VarExp("varf"))))))))));


        //tyepcheck err -> readFileStmt(new VarExp("varc"),"varc")
        IStmt ex24 = new CompStmt(new VarDeclStmt("varf",new StringType()),
                new CompStmt(new AssignStmt("varf",new ValueExp(new StringValue("test.in"))),
                        new CompStmt(new VarDeclStmt("varc",new IntType()),
                                new CompStmt(new openRFileStmt(new VarExp("varf")),
                                        new CompStmt(new readFileStmt(new VarExp("varc"),"varc"),
                                                new CompStmt( new PrintStmt(new VarExp("varc")),
                                                        new CompStmt(new readFileStmt(new VarExp("varf"),"varc"),
                                                                new CompStmt(new PrintStmt(new VarExp("varc")),new closeRFileStmt(new VarExp("varf"))))))))));


        //typecheck err
        //int v; v=4; (while (v>0) print(a);v=v-1);print(v)
        IStmt ex25 = new CompStmt(new VarDeclStmt("v",new IntType()),
                new CompStmt(new AssignStmt("v",new ValueExp(new IntValue(4))),
                        new CompStmt(new WhileStmt(new RelExp(new VarExp("v"),new ValueExp(new IntValue(0)),">"),
                                new CompStmt(new PrintStmt(new VarExp("a")),new AssignStmt("v",new ArithExp('-',new VarExp("v"),new ValueExp(new IntValue(1)))))),
                                new PrintStmt(new VarExp("v")))));

        //typecheck err
        //int a
        //int b
        //int c
        //fork(fork(print s))
        //fork(print b)
        //print c
        IStmt ex26  = new CompStmt(new VarDeclStmt("a", new IntType()), new CompStmt( new VarDeclStmt("b",new IntType()),
                new CompStmt(new VarDeclStmt("c",new IntType()), new CompStmt(new ForkStmt(new ForkStmt(new PrintStmt(new VarExp("s")))),
                        new CompStmt(new ForkStmt(new PrintStmt(new VarExp("b"))), new PrintStmt(new VarExp("c")))))));


        IStmt ex27 = new CompStmt(new VarDeclStmt("a", new RefType(new IntType())),
                new CompStmt(
                        new ForkStmt(new CompStmt( new NewStmt("a", new ValueExp(new IntValue(420))), new PrintStmt(new ReadHeapExp(new VarExp("a"))))),
                        new ForkStmt(new CompStmt( new NewStmt("a", new ValueExp(new IntValue(7))), new PrintStmt(new ReadHeapExp(new VarExp("a")))))
                )
        );

        IStmt ex28=  new CompStmt(new VarDeclStmt("a", new RefType(new IntType())),
                new CompStmt(
                        new CompStmt(new NewStmt("a", new ValueExp(new IntValue(11))), new WriteHeapStmt("a", new ValueExp(new IntValue(6)))),
                        new CompStmt(
                                new ForkStmt(new CompStmt( new CompStmt(new NewStmt("a", new ValueExp(new IntValue(420))),new WriteHeapStmt("a", new ValueExp(new IntValue(400)))), new PrintStmt(new ReadHeapExp(new VarExp("a"))))),
                                new ForkStmt(new CompStmt( new CompStmt(new NewStmt("a", new ValueExp(new IntValue(420))),new WriteHeapStmt("a", new ValueExp(new IntValue(20)))), new PrintStmt(new ReadHeapExp(new VarExp("a"))))))
                ));


        //EXAMPLE FOR MUL
        //int v1; v1=2
        //int v2; v2=3;
        //if (v1) then print mul(v1,v2) else print(v1)
        /*
        //error la if(v1)
        IStmt ex29 = new CompStmt(new VarDeclStmt("v1", new IntType()), new CompStmt( new AssignStmt("v1", new ValueExp(new IntValue(2))),
                        new CompStmt(new VarDeclStmt("v2", new IntType()), new CompStmt(new AssignStmt("v2", new ValueExp(new IntValue(3))),
                                new IfStmt(new VarExp("v1"), new PrintStmt (new MulExp(new VarExp("v1"), new VarExp("v2"))),
                                        new PrintStmt(new VarExp("v1")))))));

         */
        //int v1; v1=2
        //int v2; v2=3;
        //if (TRUE) then print mul(v1,v2) else print(v1)
        IStmt ex29 = new CompStmt(new VarDeclStmt("v1", new IntType()), new CompStmt( new AssignStmt("v1", new ValueExp(new IntValue(2))),
                new CompStmt(new VarDeclStmt("v2", new IntType()), new CompStmt(new AssignStmt("v2", new ValueExp(new IntValue(3))),
                        new IfStmt(new ValueExp(new BoolValue(true)), new PrintStmt (new MulExp(new VarExp("v1"), new VarExp("v2"))),
                                new PrintStmt(new VarExp("v1")))))));


        //EXAMPLE FOR WAIT
        //int v; v=20; wait(10); print(v*10);
        IStmt ex30 = new CompStmt(new VarDeclStmt("v", new IntType()), new CompStmt( new AssignStmt("v", new ValueExp(new IntValue(20))),
                new CompStmt(new WaitStmt(10), new PrintStmt(new ArithExp('*', new VarExp("v"), new ValueExp(new IntValue(10)))))));


        //int a
        //int b
        //int c
        //fork(fork(print a))
        //fork(print b)
        //print c
        IStmt ex31  = concatStatements(
                new VarDeclStmt("a", new IntType()),
                new VarDeclStmt("b", new IntType()),
                new VarDeclStmt("c", new IntType()),
                new ForkStmt(new ForkStmt(new PrintStmt(new VarExp("a")))),
                new ForkStmt(new PrintStmt(new VarExp("b"))),
                new PrintStmt(new VarExp("c"))
        );

        //int a
        //int b
        //if(a=b)
        //print(1)
        //else print(0)
        IStmt ex32  = concatStatements(
                new VarDeclStmt("a", new IntType()),
                new VarDeclStmt("b", new IntType()),
                new VarDeclStmt("c", new IntType()),
                new IfStmt(new RelExp(new VarExp("a"), new VarExp("b"),"=="), new PrintStmt(new ValueExp(new IntValue(1))), new PrintStmt(new ValueExp(new IntValue(0))))
        );


        //EXAMPLE FOR SWITCH
        //a=1; b=2; c=5;
        //switch(a*10)
        // (case (b*c) print(a),print(b))
        // (case (10) print(100);print(200))
        // (default print(300))
        //print(300)
        IStmt ex33 = concatStatements(
                new VarDeclStmt("a", new IntType()),
                new VarDeclStmt("b", new IntType()),
                new VarDeclStmt("c", new IntType()),
                new AssignStmt("a", new ValueExp(new IntValue(1))),
                new AssignStmt("b", new ValueExp(new IntValue(2))),
                new AssignStmt("c", new ValueExp(new IntValue(5))),
                new SwitchStmt(new ArithExp('*',new VarExp("a"), new ValueExp(new IntValue(10))),
                               new ArithExp('*', new VarExp("b"), new VarExp("c")),
                               new ValueExp(new IntValue(10)),
                               new CompStmt(new PrintStmt(new VarExp("a")), new PrintStmt(new VarExp("b"))),
                               new CompStmt(new PrintStmt(new ValueExp(new IntValue(100))), new PrintStmt(new ValueExp(new IntValue(200)))),
                               new PrintStmt(new ValueExp(new IntValue(300)))
                                ),
                new PrintStmt(new ValueExp(new IntValue(300)))
        );

        //EXAMPLE FOR SWITCH - but with typecheck err
        IStmt ex34 = concatStatements(
                new VarDeclStmt("a", new IntType()),
                new VarDeclStmt("b", new IntType()),
                new VarDeclStmt("c", new IntType()),
                new AssignStmt("a", new ValueExp(new IntValue(1))),
                new AssignStmt("b", new ValueExp(new IntValue(2))),
                new AssignStmt("c", new ValueExp(new IntValue(5))),
                new SwitchStmt(new ArithExp('*',new VarExp("a"), new ValueExp(new IntValue(10))),
                        new ArithExp('*', new VarExp("b"), new VarExp("c")),
                        new ValueExp(new IntValue(10)),
                        new CompStmt(new PrintStmt(new VarExp("s")), new PrintStmt(new VarExp("b"))),
                        new CompStmt(new PrintStmt(new ValueExp(new IntValue(100))), new PrintStmt(new ValueExp(new IntValue(200)))),
                        new PrintStmt(new ValueExp(new IntValue(300)))
                ),
                new PrintStmt(new ValueExp(new IntValue(300)))
        );

        //EXAMPLE FOR SWITCH - typecheck err
        IStmt ex35 = concatStatements(
                new VarDeclStmt("a", new IntType()),
                new VarDeclStmt("b", new IntType()),
                new VarDeclStmt("c", new IntType()),
                new VarDeclStmt("d", new BoolType()),
                new AssignStmt("a", new ValueExp(new IntValue(1))),
                new AssignStmt("b", new ValueExp(new IntValue(2))),
                new AssignStmt("c", new ValueExp(new IntValue(5))),
                new SwitchStmt(new ArithExp('*',new VarExp("a"), new ValueExp(new IntValue(10))),
                        new ArithExp('*', new VarExp("b"), new VarExp("d")), //err : d -> not int
                        new ValueExp(new IntValue(10)),
                        new CompStmt(new PrintStmt(new VarExp("a")), new PrintStmt(new VarExp("b"))),
                        new CompStmt(new PrintStmt(new ValueExp(new IntValue(100))), new PrintStmt(new ValueExp(new IntValue(200)))),
                        new PrintStmt(new ValueExp(new IntValue(300)))
                ),
                new PrintStmt(new ValueExp(new IntValue(300)))
        );

        //EXAMPLE FOR REPEAT UNTIL
        //v=0
        //repeat ( fork (print v; v=v-1) v=v+1) until v==3)
        //x=1;y=2;z=3;w=4
        //print(v*10)
        // => 0,1,2,30
        IStmt ex36 = concatStatements(
                new VarDeclStmt("v", new IntType()),
                new AssignStmt("v", new ValueExp(new IntValue(0))),
                new RepeatUntilStmt(new CompStmt(new ForkStmt(new CompStmt(new PrintStmt(new VarExp("v")), new AssignStmt(
                        "v", new ArithExp('-', new VarExp("v"), new ValueExp(new IntValue(1))))
                        )),  new AssignStmt("v", new ArithExp('+', new VarExp("v"), new ValueExp(new IntValue(1)))))
                        ,new RelExp(new VarExp("v"), new ValueExp(new IntValue(3)),"==") ),
                new VarDeclStmt("x", new IntType()),
                new VarDeclStmt("y", new IntType()),
                new VarDeclStmt("z", new IntType()),
                new VarDeclStmt("w", new IntType()),
                new AssignStmt("x", new ValueExp(new IntValue(1))),
                new AssignStmt("y", new ValueExp(new IntValue(2))),
                new AssignStmt("z", new ValueExp(new IntValue(3))),
                new AssignStmt("w", new ValueExp(new IntValue(4))),
                new PrintStmt(new ArithExp('*',new VarExp("v"), new ValueExp(new IntValue(10))))


        );


        // EXAMPLE FOR CONDITIONAL ASSIGNMENT STATEMENT
        //bool b; int c; b=true; c=b?100:200; print(c); c=(false)?100:200; print(c)
        // => 100, 200
        IStmt ex37 = concatStatements(
                new VarDeclStmt("b", new BoolType()),
                new VarDeclStmt("c", new IntType()),
                new AssignStmt("b", new ValueExp(new BoolValue(true))),
                new CondAssignStmt("c",new VarExp("b"), new ValueExp(new IntValue(100)), new ValueExp(new IntValue(200))),
                new PrintStmt(new VarExp("c")),
                new CondAssignStmt("c",new ValueExp(new BoolValue(false)), new ValueExp(new IntValue(100)), new ValueExp(new IntValue(200))),
                new PrintStmt(new VarExp("c"))
        );

        ArrayList<IStmt> arr = new ArrayList<>();
        arr.add(ex1);
        arr.add(ex2);
        arr.add(ex3);
        arr.add(ex4);
        arr.add(ex5);
        arr.add(ex6);
        arr.add(ex7);
        arr.add(ex8);
        arr.add(ex9);
        arr.add(ex10);
        arr.add(ex11);
        arr.add(ex12);
        arr.add(ex13);
        arr.add(ex14);
        arr.add(ex15);
        arr.add(ex16);
        arr.add(ex17);
        arr.add(ex18);
        arr.add(ex19);
        arr.add(ex20);
        arr.add(ex21);
        arr.add(ex22);
        arr.add(ex23);
        arr.add(ex24);
        arr.add(ex25);
        arr.add(ex26);
        arr.add(ex27);
        arr.add(ex28);
        arr.add(ex29);
        arr.add(ex30);
        arr.add(ex31);
        arr.add(ex32);
        arr.add(ex33);
        arr.add(ex34);
        arr.add(ex35);
        arr.add(ex36);
        arr.add(ex37);
        return arr;
    }

    public static void main(String[] args) {
        //int v;
        // v=2;
        // Print(v)
        IStmt ex1= new CompStmt(new VarDeclStmt("v",new IntType()),
                new CompStmt(new AssignStmt("v",new ValueExp(new IntValue(2))), new PrintStmt(new
                        VarExp("v"))));
        PrgState prg1 = new PrgState(new MyStack<>(), new MyDictionary<>(), new MyList<>(), new MyDictionary<>(), new MyHeap<>(), ex1);
        //MyIRepository repo1 = new MyRepository(prg1, "log1.txt");
        IRepository repo1 = new Repository("log1.txt");
        repo1.addProgram(prg1);
        Controller ctr1 = new Controller(repo1, true);


        //int a;
        // int b;
        // a=2+3*5;
        // b=a+1;
        // Print(b)
        IStmt ex2 = new CompStmt( new VarDeclStmt("a",new IntType()),
                new CompStmt(new VarDeclStmt("b",new IntType()),
                        new CompStmt(new AssignStmt("a", new ArithExp('+',new ValueExp(new IntValue(2)),new
                                ArithExp('*',new ValueExp(new IntValue(3)), new ValueExp(new IntValue(5))))),
                                new CompStmt(new AssignStmt("b",new ArithExp('+',new VarExp("a"), new
                                        ValueExp(new IntValue(1)))), new PrintStmt(new VarExp("b"))))));
        PrgState prg2 = new PrgState(new MyStack<>(), new MyDictionary<>(), new MyList<>(),new MyDictionary<>(), new MyHeap<>(), ex2);
        IRepository repo2 = new Repository("log2.txt");
        repo2.addProgram(prg2);
        Controller ctr2 = new Controller(repo2, true);


        //bool a;
        // int v;
        // a=true;
        // (If a Then v=2 Else v=3)
        // Print(v)
        IStmt ex3 = new CompStmt(new VarDeclStmt("a",new BoolType()),
                new CompStmt(new VarDeclStmt("v", new IntType()),
                        new CompStmt(new AssignStmt("a", new ValueExp(new BoolValue(true))),
                                new CompStmt(new IfStmt(new VarExp("a"),new AssignStmt("v",new ValueExp(new
                                        IntValue(2))), new AssignStmt("v", new ValueExp(new IntValue(3)))), new PrintStmt(new
                                        VarExp("v"))))));
        PrgState prg3 = new PrgState(new MyStack<>(), new MyDictionary<>(), new MyList<>(),new MyDictionary<>(), new MyHeap<>(), ex3);
        IRepository repo3 = new Repository("log3.txt");
        repo3.addProgram(prg3);
        Controller ctr3 = new Controller(repo3, true);


        //string varf;
        //varf="test.in";
        //openRFile(varf);
        //int varc;
        //readFile(varf,varc);print(varc);
        //readFile(varf,varc);print(varc)
        //closeRFile(varf)
        IStmt ex4 = new CompStmt(new VarDeclStmt("varf",new StringType()),
                new CompStmt(new AssignStmt("varf",new ValueExp(new StringValue("test.in"))),
                        new CompStmt(new VarDeclStmt("varc",new IntType()),
                                new CompStmt(new openRFileStmt(new VarExp("varf")),
                                        new CompStmt(new readFileStmt(new VarExp("varf"),"varc"),
                                                new CompStmt( new PrintStmt(new VarExp("varc")),
                                                        new CompStmt(new readFileStmt(new VarExp("varf"),"varc"),
                                                                new CompStmt(new PrintStmt(new VarExp("varc")),new closeRFileStmt(new VarExp("varf"))))))))));
        PrgState prg4 = new PrgState(new MyStack<>(), new MyDictionary<>(), new MyList<>(),new MyDictionary<>(), new MyHeap<>(), ex4);
        IRepository repo4 = new Repository("log4.txt");
        repo4.addProgram(prg4);
        Controller ctr4 = new Controller(repo4, true);

        /*
        string s;
        s="ana";
        print(s);
         */
        IStmt ex5 = new CompStmt(new VarDeclStmt("s",new StringType()),
                new CompStmt(new AssignStmt("s",new ValueExp(new StringValue("ana"))),new PrintStmt(new VarExp("s"))));
        PrgState prg5 = new PrgState(new MyStack<>(), new MyDictionary<>(), new MyList<>(),new MyDictionary<>(), new MyHeap<>(), ex5);
        IRepository repo5 = new Repository("log5.txt");
        repo5.addProgram(prg5);
        Controller ctr5 = new Controller(repo5, true);


         /*
        int a;
        nop;
        bool b;
        b=true;
        if(b) THEN (a=10;b=false) ELSE (a=-10;b=true;)
        print(a);
        print(b);
         */
        IStmt ex6 =  new CompStmt(new VarDeclStmt("a",new IntType()),new CompStmt(new NopStmt(),new CompStmt(
                new VarDeclStmt("b",new BoolType()), new CompStmt( new AssignStmt("b",new ValueExp(new BoolValue(true))),
                new CompStmt(new IfStmt(new VarExp("b"),new CompStmt(new AssignStmt("a",new ValueExp(new IntValue(10))),new AssignStmt("b",new ValueExp(new BoolValue(false)))),
                        new CompStmt(new AssignStmt("a",new ValueExp(new IntValue(-10))),new AssignStmt("b",new ValueExp(new BoolValue(false))))),
                        new CompStmt(new PrintStmt(new VarExp("a")),new PrintStmt(new VarExp("b"))))))));
        PrgState prg6 = new PrgState(new MyStack<>(), new MyDictionary<>(), new MyList<>(),new MyDictionary<>(), new MyHeap<>(), ex6);
        IRepository repo6 = new Repository("log6.txt");
        repo6.addProgram(prg6);
        Controller ctr6 = new Controller(repo6, true);


        //bool a;
        // int v;
        // a=true;
        // (If v>1 Then v=2 Else v=3)
        // Print(v)
        IStmt ex7 = new CompStmt(new VarDeclStmt("a",new BoolType()),
                new CompStmt(new VarDeclStmt("v", new IntType()),
                        new CompStmt(new AssignStmt("a", new ValueExp(new BoolValue(true))),
                                new CompStmt(new IfStmt(new RelExp(new VarExp("v"),new ValueExp(new IntValue(1)),">"),new AssignStmt("v",new ValueExp(new
                                        IntValue(2))), new AssignStmt("v", new ValueExp(new IntValue(3)))), new PrintStmt(new
                                        VarExp("v"))))));
        PrgState prg7 = new PrgState(new MyStack<>(), new MyDictionary<>(), new MyList<>(),new MyDictionary<>(), new MyHeap<>(), ex7);
        IRepository repo7 = new Repository("log7.txt");
        repo7.addProgram(prg7);
        Controller ctr7 = new Controller(repo7, true);


        //int v; v=4; (while (v>0) print(v);v=v-1);print(v)
        IStmt ex8 = new CompStmt(new VarDeclStmt("v",new IntType()),
                new CompStmt(new AssignStmt("v",new ValueExp(new IntValue(4))),
                        new CompStmt(new WhileStmt(new RelExp(new VarExp("v"),new ValueExp(new IntValue(0)),">"),
                                new CompStmt(new PrintStmt(new VarExp("v")),new AssignStmt("v",new ArithExp('-',new VarExp("v"),new ValueExp(new IntValue(1)))))),
                                new PrintStmt(new VarExp("v")))));
        PrgState prg8 = new PrgState(new MyStack<>(), new MyDictionary<>(), new MyList<>(),new MyDictionary<>(), new MyHeap<>(), ex8);
        IRepository repo8 = new Repository("log8.txt");
        repo8.addProgram(prg8);
        Controller ctr8 = new Controller(repo8, true);

        //Ref int v;new(v,20);Ref Ref int a; new(a,v); new(v,30);print(rH(rH(a)))
        //how it should work:
        //new(v,20)
        //new(a,v)
        //new(v,30)
        //heap: 1->20, 2->(1,int), 3->30
        /*
        IStmt ex9 = new CompStmt(new VarDeclStmt("v",new RefType(new IntType())),
                new CompStmt(new NewStmt("v",new ValueExp(new IntValue(20))),
                        new CompStmt(new VarDeclStmt("a",new RefType(new RefType(new IntType()))),
                                new CompStmt(new NewStmt("a",new VarExp("v")),new CompStmt(
                                        new NewStmt("v",new ValueExp(new IntValue(30))),
                                        new PrintStmt(new ReadHeapExp(new ReadHeapExp(new VarExp("a"))))
                                )))));

         */
        IStmt ex9 = new CompStmt(new VarDeclStmt("v",new RefType(new IntType())),
                new CompStmt(new NewStmt("v",new ValueExp(new IntValue(20))),
                        new CompStmt(new VarDeclStmt("a",new RefType(new RefType(new IntType()))),
                                new CompStmt(new NopStmt(),new CompStmt(
                                        new NewStmt("v",new ValueExp(new IntValue(30))),
                                        new PrintStmt(new ReadHeapExp(new ReadHeapExp(new VarExp("a"))))
                                )))));
        //-> error at the last print, variable "a" not declared
        //=>ExeStack:
        //print(readHeap(readHeap(a)))
        //
        //SymTable:
        //a->(0,Ref(int))    -> because a is just declared
        //v->(2,int)
        //
        //Out:
        //[]
        //FileTable:
        //
        //Heap:
        //2->30
        PrgState prg9 = new PrgState(new MyStack<>(), new MyDictionary<>(), new MyList<>(),new MyDictionary<>(), new MyHeap<>(), ex9);
        IRepository repo9 = new Repository("log9.txt");
        repo9.addProgram(prg9);
        Controller ctr9 = new Controller(repo9, true);


        //ref int v; new(v,20), print(rH(v)),new(v,40),print(rH(v))
        IStmt ex10 = new CompStmt(new VarDeclStmt("v",new RefType(new IntType())),
                new CompStmt(new NewStmt("v",new ValueExp(new IntValue(20))),
                        new CompStmt(new PrintStmt(new ReadHeapExp(new VarExp("v"))),
                                new CompStmt(new NewStmt("v",new ValueExp(new IntValue(40))),new PrintStmt(new ReadHeapExp(new VarExp("v")))))));
        PrgState prg10 = new PrgState(new MyStack<>(), new MyDictionary<>(), new MyList<>(),new MyDictionary<>(), new MyHeap<>(), ex10);
        IRepository repo10 = new Repository("log10.txt");
        repo10.addProgram(prg10);
        Controller ctr10 = new Controller(repo10, true);


        //Ref int v;new(v,20);Ref Ref int a; new(a,v);print(rH(v));print(rH(rH(a))+5)
        //Heap={1->20, 2->(1,int)}, SymTable={v->(1,int), a->(2,Ref int)} and
        //Out={20, 25}
        IStmt ex11 =  new CompStmt(new VarDeclStmt("v",new RefType(new IntType())),
                new CompStmt(new NewStmt("v",new ValueExp(new IntValue(20))),
                        new CompStmt(new VarDeclStmt("a",new RefType(new RefType(new IntType()))),
                                new CompStmt(new NewStmt("a",new VarExp("v")),new CompStmt(new PrintStmt(new ReadHeapExp(new VarExp("v"))),
                                        new PrintStmt(new ArithExp('+',new ReadHeapExp(new ReadHeapExp(new VarExp("a"))),new ValueExp(new IntValue(5)))))))));
        PrgState prg11 = new PrgState(new MyStack<>(), new MyDictionary<>(), new MyList<>(),new MyDictionary<>(), new MyHeap<>(), ex11);
        IRepository repo11 = new Repository("log11.txt");
        repo11.addProgram(prg11);
        Controller ctr11 = new Controller(repo11, true);


        //Ref int v;new(v,20); wH(v,30);print(rH(v)+5);
        //Heap={1->30}, SymTable={v->(1,int)} and Out={35}
        IStmt ex12 = new CompStmt(new VarDeclStmt("v",new RefType(new IntType())),
                new CompStmt(new NewStmt("v",new ValueExp(new IntValue(20))),
                        new CompStmt(new WriteHeapStmt("v",new ValueExp(new IntValue(30))),
                                new PrintStmt(new ArithExp('+',new ReadHeapExp(new VarExp("v")),new ValueExp(new IntValue(5)))))));
        PrgState prg12 = new PrgState(new MyStack<>(), new MyDictionary<>(), new MyList<>(),new MyDictionary<>(), new MyHeap<>(), ex12);
        IRepository repo12 = new Repository("log12.txt");
        repo12.addProgram(prg12);
        Controller ctr12 = new Controller(repo12, true);

        //int v; v=4; (while (v+0) print(v);v=v-1);print(v)
        IStmt ex13 = new CompStmt(new VarDeclStmt("v",new IntType()),
                new CompStmt(new AssignStmt("v",new ValueExp(new IntValue(4))),
                        new CompStmt(new WhileStmt(new ArithExp('+',new VarExp("v"),new ValueExp(new IntValue(0))),
                                new CompStmt(new PrintStmt(new VarExp("v")),new AssignStmt("v",new ArithExp('-',new VarExp("v"),new ValueExp(new IntValue(1)))))),
                                new PrintStmt(new VarExp("v")))));
        PrgState prg13 = new PrgState(new MyStack<>(), new MyDictionary<>(), new MyList<>(),new MyDictionary<>(), new MyHeap<>(), ex13);
        IRepository repo13 = new Repository("log13.txt");
        repo13.addProgram(prg13);
        Controller ctr13 = new Controller(repo13, true);


        //int v; Ref int a; v=10;new(a,22);
        // fork(wH(a,30);v=32;print(v);print(rH(a)));
        // print(v);print(rH(a))
        //At the end:
        //Id=1
        //SymTable_1={v->10,a->(1,int)}
        //
        //Id=10
        //SymTable_10={v->32,a->(1,int)}
        //
        //Heap={1->30}
        //Out={10,30,32,30}
        IStmt ex14 = new CompStmt(new VarDeclStmt("v",new IntType()),new CompStmt(new VarDeclStmt("a",new RefType(new IntType())),
                new CompStmt(new AssignStmt("v",new ValueExp(new IntValue(10))),new CompStmt(new NewStmt("a",new ValueExp(new IntValue(22))),
                        new CompStmt(new ForkStmt(new CompStmt(new WriteHeapStmt("a",new ValueExp(new IntValue(30))),
                                new CompStmt(new AssignStmt("v",new ValueExp(new IntValue(32))), new CompStmt(new PrintStmt(new VarExp("v")),new PrintStmt(new ReadHeapExp(new VarExp("a"))))))),
                                new CompStmt(new PrintStmt(new VarExp("v")),new PrintStmt(new ReadHeapExp(new VarExp("a")))))))));
        PrgState prg14 = new PrgState(new MyStack<>(), new MyDictionary<>(), new MyList<>(),new MyDictionary<>(), new MyHeap<>(), ex14);
        IRepository repo14 = new Repository("log14.txt");
        repo14.addProgram(prg14);
        Controller ctr14 = new Controller(repo14, true);


        //fork  - throw exception
        IStmt ex15 = new CompStmt(new VarDeclStmt("a",new IntType()),new ForkStmt(new PrintStmt(new VarExp("s"))));
        PrgState prg15 = new PrgState(new MyStack<>(), new MyDictionary<>(), new MyList<>(),new MyDictionary<>(), new MyHeap<>(), ex15);
        IRepository repo15 = new Repository("log15.txt");
        repo15.addProgram(prg15);
        Controller ctr15 = new Controller(repo15, true);


        //fork in fork
        //int a; int b;
        //fork(fork(print a))
        //fork(print b)
        //IStmt ex16 = new CompStmt(new CompStmt(new VarDeclStmt("a",new IntType()),new ForkStmt(new ForkStmt(new PrintStmt(new VarExp("a"))))), new ForkStmt(new PrintStmt(new VarExp("a"))));
        IStmt ex16 = new CompStmt(new VarDeclStmt("a",new IntType()), new CompStmt(new VarDeclStmt("b",new IntType()),
                new CompStmt(new ForkStmt(new ForkStmt(new PrintStmt(new VarExp("a")))), new ForkStmt(new PrintStmt(new VarExp("b"))))));
        PrgState prg16 = new PrgState(new MyStack<>(), new MyDictionary<>(), new MyList<>(),new MyDictionary<>(), new MyHeap<>(), ex16);
        IRepository repo16 = new Repository("log16.txt");
        repo16.addProgram(prg16);
        Controller ctr16 = new Controller(repo16, true);



        TextMenu menu = new TextMenu();
        menu.addCommand(new ExitCommand("0", "exit"));
        menu.addCommand(new RunExample("1", ex1.toString(), ctr1));
        menu.addCommand(new RunExample("2", ex2.toString(), ctr2));
        menu.addCommand(new RunExample("3", ex3.toString(), ctr3));
        menu.addCommand(new RunExample("4", ex4.toString(), ctr4));
        menu.addCommand(new RunExample("5", ex5.toString(), ctr5));
        menu.addCommand(new RunExample("6", ex6.toString(), ctr6));
        menu.addCommand(new RunExample("7", ex7.toString(), ctr7));
        menu.addCommand(new RunExample("8", ex8.toString(), ctr8));
        menu.addCommand(new RunExample("9", ex9.toString(), ctr9));
        menu.addCommand(new RunExample("10", ex10.toString(), ctr10));
        menu.addCommand(new RunExample("11", ex11.toString(), ctr11));
        menu.addCommand(new RunExample("12", ex12.toString(), ctr12));
        menu.addCommand(new RunExample("13", ex13.toString(), ctr13));
        menu.addCommand(new RunExample("14", ex14.toString(), ctr14));
        menu.addCommand(new RunExample("15", ex15.toString(), ctr15));
        menu.addCommand(new RunExample("16", ex16.toString(), ctr16));
        menu.show();
    }
}
