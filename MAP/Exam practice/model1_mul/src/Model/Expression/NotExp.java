package Model.Expression;

import Model.MyException;
import Model.ProgramState.MyIDictionary;
import Model.ProgramState.MyIHeap;
import Model.Type.BoolType;
import Model.Type.IntType;
import Model.Type.Type;
import Model.Value.BoolValue;
import Model.Value.IntValue;
import Model.Value.Value;

public class NotExp implements Exp {
    Exp exp;

    public NotExp(Exp e){
        exp=e;
    }

    @Override
    public Value eval(MyIDictionary<String, Value> tbl, MyIHeap<Value> heap) throws MyException {
        BoolValue res;
        Value v;
        v= exp.eval(tbl,heap); //value of the exp
        if (v.getType().equals(new BoolType())) {
            BoolValue b = (BoolValue) v;
            boolean val = b.getVal();
            boolean val_final = !val;
            res = new BoolValue(val_final);
            return res;
        }
        else
            throw new MyException("not exp: exp not boolean:  " + this.toString());
        //return null;
    }

    @Override
    public Exp dup() {
        return new NotExp(exp.dup());
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return null;
    }

    @Override
    public String toString() {
        return "not(" + exp.toString() + ")";
    }
}
