# ♟️PyChessGame♟️
---

>## 설명

PyChessGame은 Python의 pygame 라이브러리를 사용하여 개발한 2 Player 체스 게임입니다.<br> 
기존의 체스 룰에 몇 가지 차별적인 변화가 있어 전략적인 플레이를 즐길 수 있습니다.<br>


<br> 

---
>## 변경 사항

1. **폰 프로모션**
   - 폰이 프로모션할 때 말 승급이 랜덤으로 선택됩니다.
     >이로써 게임 전략에 더 많은 다양성을 부여합니다.

     <br> 
     

2. **체크, 체크메이트 규칙 삭제**
   - 킹을 잡을 시 게임이 즉시 종료됩니다.
     >게임 플레이 타임이 단축되어 빠른 진행이 가능합니다.

<br> 

---
>## 규칙

- 2명의 플레이어가 번갈아가며 말을 이동하여 조작합니다.
- 나이트를 제외한 모든 말은 상대방 말을 뛰어넘을 수 없습니다.
- 프로모션은 1회에 한해 폰이 체스 보드 끝에 이동했을 때 랜덤으로 이루어집니다.
- 승리 조건은 상대방 킹을 잡을 경우입니다.

# 폰(Pawn)
 > 첫 이동 시 두칸 이동 가능, 그 이외엔 앞으로만 이동 가능. 공격은 대각선으로만 가능
  
  ![image](https://github.com/Ash0704/PyChessGame/assets/123534011/5f512851-1a56-4f4f-b0ee-ada9bcbea5c5)
  ![image](https://github.com/Ash0704/PyChessGame/assets/123534011/21f54279-ac49-42fc-b94c-441d9882adee)
  
<br>

  # 나이트(Knight)
  > 한칸 후 대각선 이동 가능, 말을 뛰어넘을 수 있음
  
  ![image](https://github.com/Ash0704/PyChessGame/assets/123534011/d92f23c4-a771-482a-b976-6bfce03d532b)
  
<br>

  # 룩(Rook)
  > 상하좌우 이동 가능
  
  ![image](https://github.com/Ash0704/PyChessGame/assets/123534011/44fd61a8-ac39-4998-af9e-6ac742f8a288)
  
<br>

  # 비숍(Bishop)
  > 대각선 이동 가능
  
  ![image](https://github.com/Ash0704/PyChessGame/assets/123534011/db72a516-99f6-4561-84f4-9279af8f5f41)
  
<br>

  # 퀸(Queen)
  > 8방향 이동 가능
  
  ![image](https://github.com/Ash0704/PyChessGame/assets/123534011/bc2aaaf4-64b8-4a0c-b127-4f92ea8640f6)
  
<br>

  # 킹(King)
  > 8방향 이동 가능하며 한칸 씩 이동 가능
  
  ![image](https://github.com/Ash0704/PyChessGame/assets/123534011/7d0070c0-fb6b-4d47-8095-948191f11654)

<br> 

---
>## 구현 기능

### 화면

1. **초기 화면**
   - 게임 제목과 Play 버튼을 포함한 초기 화면이 구현되었습니다.
   - Play 버튼을 클릭하면 게임 화면으로 전환됩니다.<br>
  >   ![image](https://github.com/Ash0704/PyChessGame/assets/123534011/d4a0d2c5-cc73-4d28-b564-c2bcb5092d16)


2. **게임 화면**
   - 체스판과 말이 표시되는 게임 화면이 구현되었습니다.<br>
 >    ![image](https://github.com/Ash0704/PyChessGame/assets/123534011/d02f9b36-5c27-4644-b2cb-40d1619d785b)

  
<br>

### 좌표 기능

- [1,8], [a,h] 의 문자를 사용하여 좌표를 추가하였습니다.
- 상대방 입장에서는 좌표가 반대로 표시됩니다.
<br>

### 표시 기능

1. **선택한 말 강조**
   - 선택한 말은 붉은 테두리로 강조되어 표시됩니다.

2. **이동 가능 경로 표시**
   - 이동 가능한 경로는 초록색 원으로 표시됩니다.
   - 이동 경로에 상대방 말이 있을 경우 빨간색 원으로 표시됩니다.
<br>

### 말 이동 방식

- 폰, 나이트, 룩, 비숍, 퀸, 킹의 이동 방식이 구현되었습니다.
- 불법적인 움직임을 방지하기 위해 이동 가능 판별 함수가 적용되었습니다.
<br>

### 사운드 기능

- 게임 종료 및 말 이동 사운드가 추가되었습니다.
<br>

### 게임 종료

1. **게임 종료 조건**
   - 킹이 잡힐 시 게임이 종료됩니다.

2. **승리 메시지**
   - 텍스트로 "(Black / White) Team Wins!"가 출력됩니다.

3. **자동 종료**
   - 텍스트 출력 후 3초 뒤에 게임이 자동으로 종료됩니다.
<br>

### 프로모션

- 1회에 한해 폰이 체스 보드 끝에 이동할 때 랜덤으로 승급이 가능합니다.

<br> 

---
>## 사용 라이브러리
```
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
import sys
import random
```
<br> 

---
>## 참조
[배경화면](https://www.freepik.com/premium-photo/chess-king-chess-board-game-with-chess-figures-ai-generated_38652803.htm)<br>
[말이미지](https://github.com/Pritish934/Python_Chess_Game/tree/main/images)<br>
[효과음](https://www.mewpot.com/search/sound-effects?is_free=true)<br>

<br> 

---
>## 크레딧

✨ 오류나 희망 추가 사항이 있다면 연락주세요! 😄  
✨ **개발자 이메일:** shyun3076@naver.com

<br> 

---
>## 라이센스

이 프로젝트는 MIT LICENSE에 따라 라이센스가 부여됩니다. 자세한 내용은 [라이센스](https://github.com/Ash0704/PyChessGame/blob/main/LICENSE.md)를 참조해주세요.
