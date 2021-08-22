package Model.Statements;
MyIStack<IStmt> stk = state.getStk();
        IStmt newStmt = new IfStmt(exp1,new AssignStmt(id,exp2), new AssignStmt(id,exp3));
        stk.push(newStmt);
        return null;
import Model.Expression.Exp;
import Model.MyException;
import Model.ProgramState.MyIDictionary;
import Model.ProgramState.MyIStack;
import Model.ProgramState.PrgState;
import Model.Type.Type;
import Model.Value.Value;

public class CondAssignStmt implements IStmt {
    private String id;
    private Exp exp1;
    private Exp exp2;
    private Exp exp3;

    public CondAssignStmt(String _id, Exp e1, Exp e2, Exp e3){
        id=_id; exp1=e1; exp2=e2; exp3=e3;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {

    }

    @Override
    public IStmt dup() {
        return new CondAssignStmt(id,exp1.dup(),exp2.dup(),exp3.dup());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return typeEnv;
        //TODO - actually nu trebe :)))
    }

    @Override
    public String toString() {
        return id + "=(" + exp1.toString() + ")?" + exp2.toString() + ":" + exp3.toString();
    }
}
