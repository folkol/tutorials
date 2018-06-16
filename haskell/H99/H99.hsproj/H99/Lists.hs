module Lists where
  
import Data.List
import Control.Monad
  
myLast [head] = [head]
myLast (_:tail) = myLast tail

myLast' = head . reverse

myButLast (x:y:[]) = x
myButLast (_:tail) = myButLast tail
myButLast' = last . init

elementAt (head:_) 1 = head
elementAt (head:tail) n = elementAt tail (n - 1)

myLength [] = 0
myLength (_:tail) = 1 + myLength tail


myReverse [] = []
myReverse (head:tail) = myReverse tail ++ [head]
myReverse' = foldl (flip (:)) []


isPalindrome xs = xs == reverse xs
isPalindrome' = ap (==) reverse
isPalindrome'' = liftM2 ($) (==) reverse


data NestedList a = Elem a | List [NestedList a]
flatten (Elem a) = [a]
flatten (List a) = concatMap flatten a

compress [] = []
compress [x] = [x]
compress (x:tail@(y:_))
  | x == y    = compress(tail)
  | otherwise = x:compress(tail)

compress' = map head . group

