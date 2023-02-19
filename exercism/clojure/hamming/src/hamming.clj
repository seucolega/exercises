(ns hamming)

(defn distance [strand1 strand2]
  (if (= (count strand1) (count strand2))
    (reduce + (map-indexed (fn [index letter] (if (= letter (get strand2 index)) 0 1)) strand1)))
  )
