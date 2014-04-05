-- file: zip.hs
-- transform double line per debater csv to single line per debater csv

import Data.Functor      ((<$>))
import Data.List         (find)
import Data.List.Split   (splitOn)
import Data.Maybe        (fromJust)
import Text.CSV          (parseCSVFromFile, printCSV, CSV, Record)
import Text.Parsec.Error (ParseError)
import System.IO         (writeFile)

englishCourseID = "10CP01"
ihsCourseID     = "900012"

main :: IO ()
main = parseCSVFromFile "debaters.csv.old"
       >>= return . (>>= return . condenseDebaters)
       >>= return . (>>= return . filter (/= '"') . printCSV)
       >>= writeOrFail

writeOrFail :: (Either ParseError String) -> IO ()
writeOrFail (Right s) = writeFile "debaters.csv" s
-- writeOrFail (Right s) = putStrLn s
writeOrFail (Left pe) = putStrLn $ show pe

condenseDebaters :: CSV -> CSV
condenseDebaters = zipDebaters
                   . (\(es,is) -> (map readNames es, map readNames is))
                   . splitByCourse

splitByCourse :: CSV -> (CSV,CSV)
splitByCourse rs = (es,is)
  where es = filter ((== englishCourseID) . last) rs
        is = filter ((== ihsCourseID)     . last) rs

readNames :: Record -> Record
readNames (n:rs) = firstName:lastName:rs
  where (lastName:firstName:_) = splitOn ", " n

zipDebaters :: (CSV,CSV) -> CSV
zipDebaters ([],is) = map ((mergeDebater Nothing) . Just) is
zipDebaters (es,[]) = map ((\e -> mergeDebater e Nothing) . Just) es
zipDebaters (es,is) = (mergeDebater (Just dEng) dIHS):(zipDebaters (es',is'))
  where
    (dEng:es') = es
    dIHS       = find   (sameDebater dEng) is
    is'        = filter (not . sameDebater dEng) is

sameDebater :: Record -> Record -> Bool
sameDebater as bs = all (\(a,b) -> a == b) $ take 2 $ zip as bs

mergeDebater :: (Maybe Record) -> (Maybe Record) -> Record
-- shouldn't be called
mergeDebater Nothing Nothing       = ["","","","","",""]
mergeDebater Nothing (Just ihs)    = (names ihs) ++ ["",""] ++ (classDetails ihs)
mergeDebater (Just eng) Nothing    = (names eng) ++ (classDetails eng) ++ ["",""]
mergeDebater (Just eng) (Just ihs) = (names ihs) ++ (classDetails eng) ++ (classDetails ihs)

-- [firstName,lastName]
names :: Record -> [String]
names r = [(r !! 0),(r !! 1)]

-- [period,teacher]
classDetails :: Record -> [String]
classDetails r = [(r !! 2),(r !! 3)]
