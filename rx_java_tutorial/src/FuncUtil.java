import rx.Observable;
import rx.functions.Action1;
import rx.functions.Func1;

import java.util.concurrent.TimeUnit;

public class FuncUtil {
    public static Func1<Integer, Observable<Long>> timer() {
        return new Func1<Integer, Observable<Long>>() {
            @Override
            public Observable<Long> call(Integer integer) {
                return Observable.timer(1, TimeUnit.SECONDS);
            }
        };
    }

    public static Action1<Long> print() {
        Action1<Long> action = new Action1<Long>() {
            @Override
            public void call(Long l) {
                System.out.println(l);
            }
        };
        return action;
    }
}
