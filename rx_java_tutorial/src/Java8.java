import rx.Observable;

import java.util.concurrent.TimeUnit;

import static rx.Observable.timer;

public class Java8 {
    public static void main(String[] args) {
        Long last = Observable.range(0, 100)
                .flatMap(x -> timer(1, TimeUnit.SECONDS))
                .doOnNext(System.out::println)
                .toBlocking()
                .last();

        System.out.println(last);
    }
}
