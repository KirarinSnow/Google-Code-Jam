;;; Problem: Old Magician
;;; Language: x86
;;; Author: KirarinSnow
;;; Usage: nasm -f elf -o program.o thisfile.asm && ld -o program program.o &&
;;;          ./program <input.in >output.out


section	.data
_char:
	db	0, 0, 0, 0
_case1:
	db	"Case #"
_case2:
	db	": "
black:
	db	"BLACK", 10
white:
	db	"WHITE", 10

section	.text
global 	_start
_start:
	;; Read number of cases and store in %eax
	call	readint
	mov	ecx, 1
	mov	edx, eax
	
_main:
	push	edx
	push 	ecx

	;; Print "Case X: "
	mov	eax, 4
	mov	ebx, 1
	mov	ecx, _case1
	mov	edx, 6
	int	0x80
	
	pop	eax
	push	eax
	call	writeint
	
	mov	eax, 4
	mov	ebx, 1
	mov	ecx, _case2
	mov	edx, 2
	int	0x80

	;; Handle test case
	call	compute

	;; Increment and continue
	pop	ecx
	pop	edx
	
	inc	ecx
	cmp	ecx, edx
	jle 	_main

_exit:
	;; Terminate program
	mov	eax, 1
	mov	ebx, 0
	int	0x80

;;; Write integer in %eax
writeint:
	;; Start digit counter
	mov	ecx, 0

writeint_store:
	;; Divide to get digits, store to stack
	mov 	edx, 0
	mov	ebx, 10
	idiv	ebx
	add	edx, 48
	push	edx
	inc	ecx

	cmp	eax, 0
	jne	writeint_store

writeint_print:
	;; Print digits from stack
	pop	edx
	mov	ebx, _char
	mov	[ebx], edx
	push	ecx
	
	mov	eax, 4
	mov	ebx, 1
	mov	ecx, _char
	mov	edx, 1
	int	0x80

	pop	ecx
	dec	ecx
	cmp	ecx, 0
	jne	writeint_print
	
	ret
	
;;; Read integer into %eax
readint:
	mov	edx, 0
	push	0

readint_get:
	;; Read digits and modify return value accordingly
	pop	eax
	imul	eax, eax, 10
	add	eax, edx
	push	eax
	
	mov	eax, 3
	mov	ebx, 0
	mov 	ecx, _char
	mov	edx, 1
	int	0x80

	mov	edx, [ecx]
 	and	edx, 0xff
	sub	edx, 48
	cmp	edx, 0
	jge	readint_get
	
	pop	eax
	ret


;;; Handle test case
compute:
	call	readint
	call	readint
	mov	edx, 0
	mov	ebx, 2
	idiv	ebx
	cmp	edx, 1
	je	odd
	
even:
	mov	ecx, white
	jmp	done

odd:
	mov	ecx, black
	
done:	
	mov	eax, 4
	mov	ebx, 1
	mov	edx, 6
	int 	0x80
	ret
