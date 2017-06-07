package com.folkol;

import org.junit.Test;
import rx.Observable;
import rx.Subscriber;
import rx.functions.Action1;

import java.util.Arrays;
import java.util.List;

import static java.util.Arrays.asList;

public class AppTest {
    @Test
    public void test1() {
        Observable<String> myObservable = Observable.create(
                new Observable.OnSubscribe<String>() {
                    @Override
                    public void call(Subscriber<? super String> sub) {
                        sub.onNext("Hello, world!");
                        sub.onCompleted();
                    }
                }
        );

        Subscriber<String> mySubscriber = new Subscriber<String>() {
            @Override
            public void onNext(String s) {
                System.out.println(s);
            }

            @Override
            public void onCompleted() {
            }

            @Override
            public void onError(Throwable e) {
            }
        };

        myObservable.subscribe(mySubscriber);
        // Outputs "Hello, world!"
    }

    @Test
    public void test2() {
        Observable.just("Hello, world!").subscribe(System.out::println);
        // Outputs "Hello, world!"
    }

    @Test
    public void test3() {
        Observable.just("Hello, world!")
                .map(s -> s + " LOL")
                .map(String::hashCode)
                .subscribe(System.out::println);
        // Outputs "Hello, world!"
    }

    @Test
    public void test4() {
        List<List<String>> listOfLists = asList(
                asList("url1", "url2", "url3"),
                asList("url4", "url5"),
                asList("url6", null)
        );
        Observable.from(listOfLists)
                .flatMap(Observable::from)
                .filter(x -> x != null)
                .map(s -> s + " LOL")
                .skip(2)
                .take(5)
                .subscribe(System.out::println);
    }

    @Test
    public void test5() {
        List<List<String>> listOfLists = asList(
                asList("url1", "url2", "url3"),
                asList("url4", "url5"),
                asList("url6", null)
        );
        Observable.from(listOfLists)
                .flatMap(Observable::from)
                .filter(x -> x != null)
                .map(s -> s + " LOL")
                .skip(2)
                .take(5)
                .subscribe(System.out::println);
    }
}
