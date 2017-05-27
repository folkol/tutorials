import rx.Observable;

import java.util.concurrent.ExecutionException;
import java.util.concurrent.TimeUnit;

import static rx.Observable.timer;

public class RxOperatorComparison {
    /**
     * Both map and flatMap will return one single observable.
     * <p>
     * All items that are emitted by all observables returned by the
     * flatMap parameter will be "flattened" into a single Observable
     */
    public static void main(String[] args) throws InterruptedException, ExecutionException {
//        Observable<String> just = Observable.just("Hello1", "Hello2", "Hello3", "Hello4", "Hello5", "Hello5", "Hello5");
//        String same = just.buffer(2, 1)
//                .filter(x -> x.get(0).equals(x.get(1)))
//                .map(x -> x.get(0))
//                .toBlocking()
//                .first();

        Long last = Observable.range(0, 100)
                .flatMap(x -> timer(1, TimeUnit.SECONDS))
                .doOnNext(System.out::println)
                .toBlocking()
                .last();

//        Integer first = Observable.defer(() -> Observable.just(1, 2, 3, 4, 5))
//                .toBlocking()
//                .first();
//        System.out.println(first);


//        {
//            Observable<Integer> just = Observable.just(1, 2, 3);
//            // "just" is an Observable that will emit three items (1, 2 and 3) and then complete
//            just.subscribe(System.out::println);
//
//            // The function supplied to "map" will be called once for every item emitted by "just"
//            Observable<Integer> mapped = Observable.just(1, 2, 3).map(x -> 2 * x);
//            // "mapped" is an observable that will emit three items (2, 4 and 6) and then complete
//            mapped.subscribe(System.out::println);
//
//            // The function supplied to "flatMap" will be called once for every item emitted by "just"
//            Observable<Integer> flatMapped1 = Observable.just(1, 2, 3).flatMap(x -> Observable.just(2 * x));
//            // "flatMapped1" an observable that will emit three items (2, 4 and 6) and then complete
//            flatMapped1.subscribe(System.out::println);
//
//            // The function supplied to "flatMap" will be called once for every item emitted by "just"
//            Observable<Integer> flatMapped2 = Observable.just(1, 2, 3).flatMap(x -> Observable.just(x, x));
//            // "flatMapped2" an observable that will emit six items (1, 1, 2, 2, 3 and 3) and then complete
//            flatMapped2.subscribe(System.out::println);
//        }
//
//
//        {
//            Observable<Long> timer = Observable.timer(1, TimeUnit.SECONDS);
//            timer.map(x -> x + 666)
//                    .doOnNext(System.out::println)
//                    .collect()
//                    .ignoreElements()
//                    .toBlocking();
//        }
//
//        System.out.println("Hello");
//        Thread.sleep(2000);


//        rx.functions.Func1 someFunc = null; // Mapping function
//
//        Observable A;
//        Observable B = A.map(someFunc);
//
//        A.doOnNext(x -> {
//            Object mappedX = someFunc(x);
//            B.emit(mappedX);
//        })


//        rx.functions.Func1 someFunc = null; // Mapping function
//
//        Observable A;
//        Observable B = A.flatMap(someFunc);
//
//        A.doOnNext(x -> {
//            x.doOnNext(y -> {
//                Object mappedY = someFunc(y);
//                B.emit(mappedY);
//            })
//        })


//        Observable.just("apa")
//                .flatMap(s -> Observable.just(s + "nisse"))
//                .observeOn(Schedulers.io())
//                .flatMap(s -> {
//                    Observable.just("olle").toBlocking().singleOrDefault(null);
//                    System.out.println(s);
//                    return Observable.empty();
//                })
//                .subscribe();
//
//        Thread.sleep(2000);
    }

    // Imperative style list dual to flatMap
    // List input =
    // [
    //      [1, 2, 3],          // Return value of first flatMap function call
    //      [2, 2, 2],          // Return value of second flatMap function call
    //      [5, 5, 5, 5, 5, 5]  // Return value of third flatMap function call
    // ];
    // List result = []
    // for(List l : input) {
    //      for(Item i : l) {
    //          result.add(i);
    //      }
    // }
}
