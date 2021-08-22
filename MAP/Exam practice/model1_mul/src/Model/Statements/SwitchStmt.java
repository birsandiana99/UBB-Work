package Model.Statements;

import Model.Expression.Exp;
import Model.Expression.RelExp;
import Model.MyException;
import Model.ProgramState.MyIDictionary;
import Model.ProgramState.MyIHeap;
import Model.ProgramState.MyIStack;
import Model.ProgramState.PrgState;
import Model.Type.Type;
import Model.Value.Value;


public class SwitchStmt implements IStmt {
    private Exp exp;
    private Exp exp1;
    private Exp exp2;
    private IStmt stmt1;
    private IStmt stmt2;
    private IStmt stmt3;

    public SwitchStmt(Exp e, Exp e1, Exp e2, IStmt s1, IStmt s2, IStmt s3){
        exp=e;
        exp1=e1;
        exp2=e2;
        stmt1=s1;
        stmt2=s2;
        stmt3=s3;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> stk = state.getStk();
        IStmt newStmt = new IfStmt(new RelExp(exp,exp1,"=="), stmt1, new IfStmt(new RelExp(exp,exp2,"=="),stmt2,stmt3));
        stk.push(newStmt);
        return null;
    }

    @Override
    public IStmt dup() {
        return new SwitchStmt(exp.dup(),exp1.dup(),exp2.dup(), stmt1.dup(),stmt2.dup(),stmt3.dup());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        IStmt newStmt = new IfStmt(new RelExp(exp,exp1,"=="), stmt1, new IfStmt(new RelExp(exp,exp2,"=="),stmt2,stmt3));
        return newStmt.typecheck(typeEnv);
        //TODO
    }

    @Override
    public String toString() {
        return "switch(" + exp.toString() + ")\n" + "(case " + exp1.toString() + " : " + stmt1.toString() + ") \n" +
                "(case " + exp2.toString() + " : " + stmt2.toString() + ") \n" +
                "(default : " + stmt3.toString() + ")";
    }
}
