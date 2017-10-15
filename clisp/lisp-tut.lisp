;;;; Describe Program
;;; Basic Comment
(print
 ;; Indented Comment
 "Hello") ; End-of-line Comment

#||
Multiline comment
||#

(format t ; If string, stream or t, return nil. Otherwise return formatted string
        "Hello world ~%") ; ~ = directive. ~% = newline

(print "What's your name")
(defvar *name* (read)) ; * is convention for global variable. Case insensitive.
(defun hello-you (name)
  (format t "Hello ~a! ~%" name))  ; ~a consumes one argument, ~10@a whitespace-fill. Right without @.

(setq *print-case* :capitalize) ; Default is all upper case. :upcase, :downcase, :capitalize
(hello-you *name*) ; Call hello-you.

;;; Form is a list with a function as first item. Can be nested.
(+ 5 (- 6 2))

;;; Almost everything in Lisp is a list. Which is a linked list (cons-cells) ending with nil.

(defvar *number* 0) ; Global. Scoped variables can be set with "let"
(setf *number* 6) ; Update variable value.

(format t "Number with commas ~:d" 100000000000)
(format t "PI to 5 characters ~5:d~%" 3.141503)


(+ 5 4)
(- 5 4)
(* 5 4)
(rem 5 4)
(mod 5 4)
(log 5 4)
(eq 'dog 'dog) ; Equality
(floor 5.5)
(ceiling 5.5)
(max 5 10)
(min 5 10)
(oddp 15)
(evenp 15)
(numberp 2)

;;; defvar evaluates the parameter always, defvar only if not bound
(defparameter *name* 'Derek) ; 'Derek is a symbol. 
(format t "(eq *name* 'Derek) = ~d ~%" (eq *name* 'Derek))

(format t "(equalp 1.0 1) = ~d ~%" (equalp 1.0 1))
(format t "(equalp \"Derek\" \"derek\") = ~d ~%"
        (equalp "Derek" "derek")) ; T... case insensitive!

(defvar *age* 18)

;;; > < = and or not
(if (= *age* 18)
    (format t "You can vote~%")
    (format t "You can't vore~%"))

(if (and (<= *age* 15) (>= *age* 67))
    (format t "Work if you want.~%")
    (format t "Time for work!~%"))

(defvar *num* 2)
(defvar *num-2* 2)
(defvar *num-3* 2)

(if (= *num* 2)
    (progn ; Evalutates a number of forms, discards all values but the last one.
      (setf *num-2* (* *num-2* 2))
      (setf *num-3* (* *num-3* 3)))
    (format t "Not equal to 2~%"))

(defun get-school (age)
  (case age
    (5 (print "Kindergarten"))
    (6 (print "First Grade"))
    (otherwise (print "middle school"))))

(get-school 5)

(terpri) ; newline

(when (= *age* 18)
  (setf *num-3* 18)
  (format t "Go to college, you're ~d ~%" *num-3*))

(unless (= *age* 18)
  (setf *num-3* 18)
  (format t "Go to college, you're ~d ~%" *num-3*))

(defvar *college-ready* nil)

(cond  ((>= *age* 18)
        (setf *college-ready* 'yes)
        (format t "Ready for college ~%"))
       ((< *age* 18)
        (setf *college-ready* 'no)
        (format f "Not ready for college ~%"))
       (t (format t "Don't know ~%")))

(loop for x from 1 to 10
   do (print x))

(setq x 1)
(loop
   (format t "~d ~%" x)
   (setq x (+ x 1))
   (when (> x 10) (return x)))

(loop for y from 100 to 110 do
     (format t "On number: ~d ~%" y))

(dotimes (y 12)
  (print y))

(cons 'Foo 'Bar)
(cons 'superman 'batman)

(list 'superman 'batman 'flash)

(cons 'aquaman '(superman batman))

(format t "First = ~a ~%" (car '(superman batman aquaman)))
(format t "Everything else = ~d ~%" (cdr '(superman batman aquaman)))
;;; first of the second of the second of the second etc... right-to-left
(format t "2nd Item = ~a ~%" (caddr '(superman batman aquaman flash joker)))

(format t "Is it a list = ~a ~%" (listp '(batman superman)))
(format t "Is three in list = ~a ~%" (if (member 3 '(2 4 6)) 't nil))
(format t "Is three in list = ~a ~%" (if (member 4 '(2 4 6)) 't nil))

(defparameter *nums* '(2 4 6))
(push 1 *nums*)
(format t "2nd Item in ~a = ~a ~%" *nums* (nth 2 *nums*))

;;; plist is a list with symbols that label data
(defvar superman (list :name "Superman" :secret-id "Clark Kent"))
(defvar *hero-list* nil) ; nil = empty list
(push superman *hero-list*)
(dolist (hero *hero-list*)
  (format t "~{~a: ~a ~}~%" hero)) ; ~{ ~} format each key-value-pair

(defparameter *heroes*
  '((Superman (Clark Kent))
    (Flash (Barry Allen))
    (Batman (Bruce Wayne))))
(format t "Superman Data ~a~%" (assoc 'superman *heroes*))
(format t "Superman is ~a~%" (cadr (assoc 'superman *heroes*)))

(defparameter *hero-size*
  '((Superman (6 ft 3 in) (230 lbs))
    (Flash (6 ft 0 in) (190 lbs))
    (Batman (6 ft 2 in) (210 lbs))))
(format t "Superman is ~a~%" (cadr (assoc 'Superman *hero-size*))))

(defun hello ()
  (print "Hello")
  (terpri))

(defun get-avg (num-1 num-2)
  (/ (+ num-1 num-2) 2))
(format t "Avg 10 % 50 = ~a ~%" (get-avg 10 50))
(defun print-list (w x &optional y z) ; y and z is optional, defaults to nil
  (format t "List = ~a ~%" (list w x y z)))
(print-list 1 2 3)

(defvar *total* 0)
(defun sum (x y &rest nums) ; all variables after x and y...
  (print x)
  (print y)
  (print nums)
  (setf *total* (+ *total* x))
  (setf *total* (+ *total* y))
  (dolist (num nums)
    (setf *total* (+ *total* num)))  
  (format t "Sum = ~a~%" *total*))
(sum 1 2 31 312 21 31 3)

(defun print-list (&optional &key x y z)
  (format t "List: ~a ~%" (list x y z))) ; Return value, last expression.
(print-list :x 1 :y 2)

(defun difference (num1 num2)
  (return-from difference (- num2 num1)))
(difference 2 3)

(defun get-hero-data (size)
  (format t "~a~%" `(,(caar size) is ,(cadar size) and ,(cddar size))))  ; quasi-quote. Quoted, but escaped with ,
(get-hero-data *hero-size*)

(format t "A number ~a ~%" (mapcar #'numberp '(1 2 3 f g))) ; Map 'is a number' over list. #'foo = (function foo)

(flet ((func-name (arguments)
         ;; function body
         )
       body))

;;; Evaluate a bunch of forms with these local function definitions
(flet
    ((double-it (num)
       (* num 2))
     (triple-it (num)
       (* num 3)))
  (format t "Double 10 = ~d~%" (double-it 10)) 
  (format t "Triple 10 = ~d~%" (triple-it 10))
  (format t "Double % Triple 10 = ~d~%" (triple-it (double-it 10))))

;;; Same as flet, but the bindings are valid inside the defined functions as well as the flet body...
(labels ((double-it (num)
           (* num 2))
         (triple-it (num)
           (* (double-it num) 3)))
  (format t "Double & Triple 2 = ~d~%" (triple-it 3)))

;;; Return multiple values from a function
(defun squares (num)
  (values (expt num 2) (expt num 3))) ; expt = exponent
(multiple-value-bind (a b) (squares 2)
  (format t "2^2 = ~d 2^3 = ~d~%" a b))

(defun times-3 (x) (* 3 x))
(defun times-4 (x) (* 4 x))
(defun multiples (mult-func max-num)
  (dotimes (x max-num)
    (format t "~d : ~d ~%" x (funcall mult-func x))))
(multiples (function times-4) 2)
(multiples #'times-4 2)
(multiples #'times-4 10)

(mapcar (lambda (x) (print (* x 2))) '(1 2 3))

;;; Trivial macros
(defmacro eight () (+ 3 5)) ; Evaluates (+ 3 5) to 8, and defines the macro eight to transform to 8.
(defmacro eight () '(+ 3 5)) ; Defines the macro eight to transform to (+ 3 5), to be evaluated in runtime.
(defvar a 10)
(defvar b 11)
(setq b 1)
(if (= a b)
    (print "yay")
    (print "nay"))
(defmacro yay-if-equals (a b)
  `(progn
     (print (type-of ,a))
     (print (type-of ,b))
     (print a)
     (print b)
     (if (= ,a ,b)
         (print "yay")
         (print "nay"))))
(yay-if-equals a b)

;;; Macro is 'evaluated' during compile time, the body is NOT evaluated before the macro is called
(defvar *num* 2)
(defvar *num-2* 2)

(if (= *num* 2)
    (progn
      (setf *num-2* 2)
      (format t "*num-2* = ~d ~%" *num-2*))
    (format t "Not equal to 2~%"))

;;; Macros takes source code and generates source code
(defmacro ifit (condition &rest body)
  `(if ,condition (progn ,@body) (format t "Can't Drive...~%")))

(setf *age* 16)
(ifit (>= *age* 16)
      (format t "You are over 16. ")
      (format t "Time to drive!")
      (terpri))

(defmacro print-code (&rest body)
  '(body))
(print-code (print 'Hello-world))


;;; Python-like list comprehension
(defun range-helper (x)
  (if (= x 0)
      (list x)
      (cons x (range-helper (- x 1)))))

(defun range (x)
  (reverse (range-helper (- x 1))))

;; equivalent to the python example:
;; define a variable
(defvar divisibleByTwo nil)

;; loop from 0 upto and including 9
(loop for x in (range 10)
   ;; test for divisibility by two
   if (= (mod x 2) 0) 
   ;; append to the list
   do (setq divisibleByTwo (append divisibleByTwo (list x))))

(defmacro lcomp (expression for var in list conditional conditional-test)
  ;; create a unique variable name for the result
  (let ((result (gensym)))
    ;; the arguments are really code so we can substitute them 
    ;; store nil in the unique variable name generated above
    `(let ((,result nil))
       ;; var is a variable name
       ;; list is the list literal we are suppose to iterate over
       (loop for ,var in ,list
            ;; conditional is if or unless
            ;; conditional-test is (= (mod x 2) 0) in our examples
            ,conditional ,conditional-test
            ;; and this is the action from the earlier lisp example
            ;; result = result + [x] in python
            do (setq ,result (append ,result (list ,expression))))
           ;; return the result 
       ,result)))

(lcomp x for x in (range 666) if (= (mod x 2) 0))


(defun add (num1 num2)
  (let ((sum (+ num1 num2)))
    (format t "~a + ~a = ~a ~%" num1 num2 sum)))

(defmacro letx (var val &rest body)
  `(let ((,var , val)) ,@body))

(defun subtract (num1 num2)
  (letx dif (- num1 num2)
        (format t "~a - ~a = ~a ~%" num1 num2 dif)))

#|| Expands to:

(defun subtract (num1 num2)
  (let ((dif (- num1 num2)))
        (format t "~a - ~a = ~a ~%" num1 num2 dif))))

||#

(subtract 2 3)


;;; Classes
(defclass animal()
  (name
   sound))

(defparameter *dog* (make-instance 'animal))
(setf (slot-value *dog* 'name) "Spot")
(setf (slot-value *dog* 'sound) "Woof")
(print *dog*)

(format t "~a says ~a~%"
        (slot-value *dog* 'name)
        (slot-value *dog* 'sound))

(defclass mammal ()
  ((name
    :initarg :name
    :initform (error "Must provide a name"))
   (sound
    :initarg :sound
    :initform "No Sound"
    :accessor mammal-sound  ; :reader + :writer
)))

(defparameter *king-kong*
  (make-instance 'mammal :name "King Kong" :sound "Rawr"))
(format t "~a says ~a ~%"
        (slot-value *king-kong* 'name)
        (slot-value *king-kong* 'sound))

(defparameter *fluffy*
  (make-instance 'mammal :name "Fluffy" :sound "Meep"))
(defmacro mprint (val)
  `(format t "~a says ~a ~%"
        (slot-value ,val 'name)
        (slot-value ,val 'sound)))
(mprint *fluffy*)
(format t "~a says ~a ~%"
        (slot-value *king-kong* 'name)
        (slot-value *king-kong* 'sound))

(defgeneric make-sound (mammal))
(defmethod make-sound ((the-mammal mammal)) ; In CL, methods do not belong to a class, but to a generic function...
  (format t "~a says ~a ~%"
        (slot-value the-mammal 'name)
        (slot-value the-mammal 'sound)))
(make-sound *king-kong*)
(make-sound *fluffy*)

(defgeneric (setf mammal-name) (value the-mammal))
(defmethod (setf mammal-name) (value (the-mammal mammal))  ; Setter
  (setf (slot-value the-mammal 'name) value))
(defgeneric mammal-name (the-mammal))
(defmethod mammal-name ((the-mammal mammal))
  (slot-value the-mammal 'name))
(mammal-name *fluffy*)
(setf (mammal-name *fluffy*) "Rofl")
(mammal-name *fluffy*)
(setf (mammal-name *fluffy*) "Fluffy")

;;; Automatically generated getters and setters
(setf (mammal-sound *king-kong*) "APAN")

(format t "I am ~a ~%" (mammal-name *king-kong*))


;;; Inheritance  (defclass name (superclass1 superclass2)
(defclass dog (mammal) ())
(defparameter *rover*
  (make-instance 'dog :name "Rover" :sound "Woff"))
(mprint *rover*)


(defparameter names (make-array 3))
(setf (aref names 1) 'Bob)
(aref names 1)
(format t "~a ~%" (aref names 1))

;;; Arrays
(setf num-array
      (make-array '(3 3)
                  :initial-contents '((0 1 2) (3 4 5) (6 7 8))))
(dotimes (x 3)
  (dotimes (y 3)
    (print (aref num-array x y))))

;;; Hashes
(defparameter people (make-hash-table))
(setf (gethash '102 people) '(Paul Smith))
(setf (gethash '103 people) '(Sam Smith))

(format t "~a ~%" (gethash '102 people))
(maphash #'(lambda (k v) (format t "~a = ~a~%" k v)) people)
(remhash '103 people)


;;; structs
(defstruct customer name address id)
(setq paulsmith (make-customer
                 :name "Paul Smith"
                 :address "123 Main"
                 :id 1000))
(format t "~a ~%" (customer-name paulsmith))
(setf (customer-address paulsmith) "125 Main")
(write paulsmith)
(setq sally-smith-1001 (make-customer
                        :name "Sally Smith"
                        :address "126 Main"
                        :id 1001))
(print sally-smith-1001)


;;; File I/O
(with-open-file (my-stream
                 "test.txt" ; ./.emacs.d/auto-save-list/test.txt
                 :direction :output
                 :if-exists :supersede)
  (princ "Some random Text" my-stream)))

(let ((in (open "test.txt" :if-does-not-exist nil)))
  (when in
    (loop for line = (read-line in nil)
       while line do (format t "~a~%" line))
    (close in)))
