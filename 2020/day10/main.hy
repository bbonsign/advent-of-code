(import [input [inp sample sample2]])

(setv inp (sorted inp)
      sample (sorted sample)
      sample2 (sorted sample2))

(defn part1 [numbers]
  (setv diffs (lfor i (range (- (len numbers) 1))
                    (- (get numbers (+ i 1)) (get numbers i))))
  (setv d {1 0  3 0})
  (for [diff diffs] (do
                      (if (= 1 diff)
                        (+= (get d 1) 1))
                      (if (= 3 diff)
                        (+= (get d 3) 1))))
  [d   (* (+ 1 (get d 1)) (+ 1 (get d 3)))])
