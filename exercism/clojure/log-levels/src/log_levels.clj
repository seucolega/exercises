(ns log-levels
  (:require [clojure.string :as str]))

(defn split-s
  ""
  [s]
  (str/split s #": ")
  )

(defn message
  "Takes a string representing a log line
   and returns its message with whitespace trimmed."
  [s]
  (-> s (split-s) (second) (str/trim))
  )

(defn log-level
  "Takes a string representing a log line
   and returns its level in lower-case."
  [s]
  (let [level (-> s (split-s) (first))]
    (-> level (subs 1 (- (count level) 1)) (str/lower-case)))
  )

(defn reformat
  "Takes a string representing a log line and formats it
   with the message first and the log level in parentheses."
  [s]
  (format "%s (%s)" (message s) (log-level s))
  )
