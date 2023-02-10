(ns cars-assemble)

(defn production-rate
  "Returns the assembly line's production rate per hour,
   taking into account its success rate"
  [speed]
  (let [produced 221.
        rate     (cond
                  (>= speed 10) 0.77
                  (>= speed 9) 0.8
                  (>= speed 5) 0.9
                  (>= speed 1) 1
                  :else 0)]
    (* speed produced rate))
  )

(defn working-items
  "Calculates how many working cars are produced per minute"
  [speed]
  (-> (production-rate speed) (quot 60) (int))
  )
