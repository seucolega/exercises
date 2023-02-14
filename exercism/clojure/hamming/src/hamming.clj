(ns hamming)

(defn distance [strand1 strand2]
  (let [strand1-count (count strand1)
        same-count    (= strand1-count (count strand2))
        validated     (and same-count (> strand1-count))
        equals        (if validated (keep-indexed #(if (= %2 (nth strand2 %1)) %2) strand1))
        equals-count  (if (nil? equals) 0 (count equals))
        distance      (- strand1-count equals-count)]
    (if same-count distance))
)
