addThree :: Int -> Int -> Int -> Int
addThree x y z = x + y + z

myEq :: (Eq a) => a -> a -> Bool
myEq x y = x == y

fib :: Int -> Int -> Int
fib x y = fib y x+y

callFib = fib 0 1


printList :: (Show a) => [a] -> String
printList [] = "done"
printList (h:tail) = printList tail


reverseIt :: [a] -> [a]
reverseIt [] = []
reverseIt (h:t) = (reverseIt t) ++ [h]

-- TODO: make arg2 optional
reverseIt' :: [a] -> [a] -> [a]
reverseIt' [] end = end
reverseIt' (h:t) reversed = reverseIt' t ([h] ++ reversed)


pivot :: [a] -> a
pivot list = list !! ((length list) `div` 2)

-- my impl
quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort list = (quicksort [x | x <- list, x < piv]) ++ [x | x <- list, x == piv] ++ (quicksort [x | x <- list, x > piv])
    where piv = list !! ((length list) `div` 2)

-- textbook impl
quicksort2 :: (Ord a) => [a] -> [a]
quicksort2 []       = []
quicksort2 (p:xs)   = (quicksort2 lesser) ++ [p] ++ (quicksort2 greater)
    where
        lesser = filter (< p) xs
        greater = filter (>= p) xs
        

-- guard. more powerful pattern matching. can be expression
guardMe :: String -> String
guardMe attacker
    | attacker == "assasin" = "Oops."
    | attacker == "dragon" = "RUN!"
    | attacker == "transient" = "Bugger off, you!"
    | otherwise = "I'll defend you!"

guardYou :: Integer -> String
guardYou dmg
    | dmg < 1 = "you hit like a wimp."
    | dmg `mod` 7 == 0 = "you're amazing!"
    | dmg > 10 = "a victory"
    | otherwise = "you take damage"

-- where. function value
circumference :: Float -> Float
circumference r = pi * (sq r)
    where sq r = r ^ 2

-- let. local value
circumference2 :: Float -> Float
circumference2 r = 
    let myPi = 3.14159
        sq r = r ^ 2
    in myPi * sq r

-- case. an expression
casement jokes =
    case jokes
    of  "fart" -> "bad"
        "pun" -> "better"
        "Shakespearian" -> "best"
        a -> "unknown"


-- Chapter 4

fib2 :: Int -> Int
fib2 0 = 0
fib2 1 = 1
fib2 n = fib2 (n-2) + fib2 (n - 1)


-- [0, 1, 2, 3, 4, 5]
myMax :: (Ord a) => [a] -> a
myMax [x] = x
myMax (x:xs)
    | x > myMax(xs) = x
    | otherwise = myMax(xs)

myMax2 :: (Ord a) => [a] -> a
myMax2 [x] = x
myMax2 (x:xs) = singleMax x (myMax xs)

singleMax x y
    | x > y = x
    | x < y = y
    | otherwise = error "equal"

replicate' :: Int -> a -> [a]
replicate' 0 y = []
replicate' x y = y : replicate' (x-1) y

reverse' :: [a] -> [a]
reverse' [] = []
reverse' (x:xs) = reverse' xs ++ [x]

take' :: Int -> [a] -> [a]
take' n _
    | n <= 0 = []
take' _ [] = []
take' n (x:xs) = x : take' (n-1) xs

repeat' :: a -> [a]
repeat' a = a : repeat' a
