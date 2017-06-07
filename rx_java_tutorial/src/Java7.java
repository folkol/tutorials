import rx.Observable;

public class Java7 {
    public static void main(String[] args) {
        Long last = Observable.range(0, 100)
                .flatMap(FuncUtil.timer())
                .doOnNext(FuncUtil.print())
                .toBlocking()
                .last();

        System.out.println(last);
    }
}
