; Problem: Old Magician
; Language: Clojure
; Author: KirarinSnow
; Usage: clojure thisfile.clj <input.in >output.out


(defn compute []
  (let [w (read)
        b (read)]
    (if (= (mod b 2) 1) "BLACK" "WHITE")))


(doseq [i (range (read))]
  (println (format "Case #%d: %s" (inc i) (compute))))
