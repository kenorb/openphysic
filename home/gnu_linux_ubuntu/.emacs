;; plus de beep mais ca clignote
(setq visible-bell t)

;; barre de defilement
;;(scroll-bar-mode -1) ;; supprimer la barre
;;(set-scroll-bar-mode 'right) ;; nil left right

;; afficher le numero de colonne en plus du numero de ligne
(column-number-mode t) ;; ou (column-number-mode 1)

(autoload 'scilab-mode "scilab" "Enter Scilab mode." t)
(setq auto-mode-alist (cons '("\\(\\.sci$\\|\\.sce$\\)" . scilab-mode) auto-mode-alist))
(autoload 'scilab-shell "scilab" "Interactive Scilab mode." t)

;; User Level customizations (You need not use them all):
(setq scilab-indent-function t)      ; if you want function bodies indented
;;   (setq scilab-verify-on-save-flag nil) ; turn off auto-verify on save
;;   (defun my-scilab-mode-hook ()
;;     (setq fill-column 76))           ; where auto-fill should wrap
;;   (add-hook 'scilab-mode-hook 'my-scilab-mode-hook)
;;   (defun my-scilab-shell-mode-hook ()
;;      '())
;;   (add-hook 'scilab-shell-mode-hook 'my-scilab-shell(-mode-hook)

(custom-set-variables
 '(case-fold-search t)
 '(current-language-environment "Latin-9")
 '(default-input-method "latin-9-prefix")
 '(ecb-options-version "2.27")
 '(ecb-tip-of-the-day nil)
 '(font-latex-match-function-keywords (quote ("begin" "end" "pagenumbering" "thispagestyle" "pagestyle" "nofiles" "includeonly" "bibliographystyle" "documentstyle" "documentclass" "newenvironment" "newcommand" "newlength" "newtheorem" "newcounter" "renewenvironment" "renewcommand" "renewlength" "renewtheorem" "renewcounter" "usepackage" "fbox" "mbox" "sbox" "vspace" "hspace" "thinspace" "negthinspace" "enspace" "enskip" "quad" "qquad" "nonumber" "centering" "TeX" "LaTeX" "frametitle" "pause")))
 '(font-latex-match-title-2-keywords (quote ("section" "Section")))
 '(font-latex-match-title-3-keywords (quote ("subsection" "Subsection")))
 '(font-latex-match-title-4-keywords (quote ("subsubsection" "Subsubsection")))
 '(global-font-lock-mode t nil (font-lock))
 '(load-home-init-file t t)
 '(transient-mark-mode t))
(custom-set-faces)

;; raccourci pour compiler
(global-set-key [f5] `compile)
;; raccourci pour lancer une commande shell (executer)
(global-set-key [f6] `shell-command)

;; LaTeX par s.cls (TO DO)
;; (setq latex-mode-hook ;fonction appelee des que l'on ouvre un fichier .tex

;;       `(lambda ()
;; 	 (unless (zerop (call-process-shell-command "make view-ps"))
;; 	   (error "'make view-ps' returned an error!")))
;; )


;; copier coller � la windows pour Emacs
;; pas pour XEmacs
(pc-selection-mode)

;; d�placement de la fen�tre avec la roulette de la souris pour Emacs
;; pas pour XEmacs
(mouse-wheel-mode)

;; http://cedet.sourceforge.net/
;;(require 'ede)
;;(global-ede-mode t)


;; http://ecb.sourceforge.net/
;(ecb-minor-mode)

;; http://jdee.sunsite.dk/



;; Changement de buffer C-x b am�lior� pour Emacs
;; pas pour XEmacs
(iswitchb-mode)

;; Intellisense
;; Intellisense - Cedet Version 1.0 beta1 and later
;; http://cedet.sourceforge.net/intellisense.shtml
(setq semantic-load-turn-useful-things-on t)
   ;; Replace the path below with the install location.
;;   (load-file "~/cedet-VERSION/common/cedet.el")
(load-file "/usr/share/emacs/site-lisp/cedet-common/cedet.el")


;; Intellisense - Semantic Version 1.4x
;;(setq semantic-load-turn-useful-things-on t)
;;   (require 'semantic-load)


;; Raccourci pour l'intellisence
(global-set-key [f11] `semantic-analyze-possible-completions)
(global-set-key [f12] `semantic-ia-complete-symbol) ;; better (http://cedet.sourceforge.net/intellisense.shtml)


;; Raccourci plus facile pour la completion
(global-set-key [f4] `complete-symbol)


;;(require 'ucs-tables) - inutile dans la version cvs
;;(unify-8859-on-encoding-mode t) 		; les caract�res encodables en latin-9 le seront directement
;;(unify-8859-on-decoding-mode t) 		; au d�codage, les caract�res latins repr�sentables en latin-1
										; sont remapp�s, les autres passent en mule-unicode-0100-24ff
										; �a permet par exemple de comparer �� latin-1 identique � �� latin-9


;;; Spelling
(when (require 'ispell)
  (standard-display-european 1) 
  (setq ispell-program-name "aspell")
  (setq ispell-dictionary "francais")
  (setq flyspell-default-dictionary "francais")
  ;(setq TeX-open-quote "\og ")
  ;(setq TeX-open-quote "\fg ")
  (setq TeX-open-quote "�~")
  (setq TeX-close-quote "~�")
  (autoload 'flyspell-mode "flyspell" "On-the-fly spelling." t)
;  (require 'ucs-tables)
;  (unify-8859-on-encoding-mode 1)
;  (unify-8859-on-decoding-mode 1)
)


;;  (require 'ucs-tables)
;;  (unify-8859-on-encoding-mode 1)
;;  (unify-8859-on-decoding-mode 1)

(add-hook 'text-mode-hook
	  '(lambda ()
	     (flyspell-mode)
	     (turn-on-auto-fill)
))


;;;; LaTeX add-hook ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(add-hook 'LaTeX-mode-hook
	  '(lambda ()
	     (load "mon-tex.el") ;def de mes fonctions.
	     (LaTeX-math-mode)
	     (flyspell-mode)
	     (setq ispell-parser 'tex)
	     (turn-on-reftex)   ; reftex pour AUCTeX LaTeX mode
))

;(add-hook 'LaTeX-mode-hook 
;	  '(lambda () 
;	     (ispell-change-dictionary "francais")
;	     (setq TeX-open-quote "�~")
;	     (setq TeX-close-quote "~�")
;	     (auto-fill-mode t)
;	     (abbrev-mode t)
;	     (read-abbrev-file)
;	     (flyspell-mode t)
;	     (turn-on-reftex)
;	     )



;; Que faire quand on cr�e un nouveau doc .tex
;; ecriture de l'entete
;; M-x LaTeX-environment
(add-hook 'LaTeX-document-style-hook
	  '(lambda ()
	     (previous-line 1)
	     (insert "\\usepackage[french]{babel}")
	     (newline 1)
	     (insert "\\usepackage[latin1]{inputenc}")
	     (newline 1)
	     (insert "\\usepackage[T1]{fontenc}")
	     (newline 1)
	     (insert "\\usepackage{a4wide}")
	     (newline 1)
	     (next-line 1)
	     )
	  )

;; r�soud le probl�me des accents avec aspell et flyspell
(setq ispell-dictionary-alist
      (cons
       '("fr_FR-lrg" "[A-Za-z���������������������������]"
  "[^A-Za-z���������������������������]" "[-']" t nil "~list"
  iso-8859-1)
       ispell-dictionary-alist))

(ispell-change-dictionary "fr_FR-lrg")
(ispell-change-dictionary "fr_FR-lrg")


(global-set-key [f2] 'flyspell-mode)
(global-set-key [f3] 'flyspell-buffer)

(add-to-list 'auto-mode-alist
               '(".java$" . java-mode))

;; D�marrage du Shell dans Emacs
;; (eshell)
;; (shell)
;;(term "/bin/bash")