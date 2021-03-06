- [주문창조 Workflow](#주문창조-workflow)
- [주문갱신 Workflow](#주문갱신-workflow)
- [Job창조 Workflow](#Job창조-workflow)
- [Job갱신 Workflow](#Job갱신-workflow)

### 주문창조 Workflow
- 주문은 웹매니저와 고객앱을 리용하여 창조할수 있다.
- 통지기능
   - 고객이 앱을 리용하여 주문을 창조하는 경우 통지를 받지않는다. [구현됨]
   - 고객은 웹매니저에서 주문이 창조되였을 경우에 그에 대해 통지를 받는다. [구현됨]

### 주문갱신 Workflow
- 주문은 웹매니저와 고객앱을 리용하여 갱신할수 있다.
- 갱신로직
   - 이미 끝난 주문과 배차가 끝난 주문에 관해서는 갱신을 할수 없다. [구현됨]
   - 주문에 대한 아무런 Job이 창조되지 않은 경우 수정가능 [구현됨]
   - 주문한 대한 Job이 창조되는 경우 고객, 원천지, 목적지, 정류소메타(is_same_station)들은 변경할수 없다. 창조된 Job의 물품에 대해서는 삭제를 할수 없으며 수량만 변경할수 있으나 배차된 수량보다 작게 되면 갱신이 될수 없다. 새로운 물품은 더 창조할수 있다. [구현됨]

- 통지기능
   - 고객이 앱을 리용하여 주문을 갱신하는 경우 통지를 받지않는다. [구현됨]
   - 웹매니저에서 주문이 갱신되는경우
      - 고객이 바뀌지 않는 경우 고객은 주문갱신통지를 받는다. [구현됨]
      - 고객이 바뀌는 경우 새 고객은 주문창조통지를 이전고객은 주문삭제통지를 받는다. [구현됨]

### 주문삭제 Workflow
- 주문은 웹매니저와 고객앱을 리용하여 삭제할수 있다.
- 삭제로직
   - 배차가 시작된 주문에 관해서는 삭제할수 없다. 즉 배차가 시작되지 않은 주문에 관해서만 삭제가능하다.[구현됨]
- 통지기능
   - 웹매니저에서 주문이 삭제되는 경우 고객은 주문삭제통지를 받는다. [구현됨]

### Job창조 Workflow
- Job은 웹매니저에서 창조할수 있다.
- 통지기능
   - Job이 창조되면 기사, 부기사, 고객은 Job창조 통지를 받는다. [구현됨]

### Job갱신 Workflow
- Job은 웹매니저에서 갱신할수 있다.
- 갱신로직
   - 이미 끝난 Job에 관해서는 갱신을 할수없다. [구현됨]
   - 아직 시작하지 않은 Job에 관해서는 모든 마당들이 수정가능하다. [구현됨]
   - Job이 시작한후에는 차량은 변경시킬수 없다. [구현됨]
   - Job이 적재소에 도착하기전까지는 차량은 제외한 모든 마당이 수정가능하다.
   - Job이 적재소에 도착한후에는 적재할 물품에 대한 변경은 진행할수 없다.[구]
   - 이미 지나온 경로에 대한 변경은 진행할수 없다.[구]
   - Job이 해당한 목적지까지 도작하지 않았을 경우에 그목적지에 부리는 량은 변경가능하다.
   - Job이 시작한후에 기사, 부기사를 변경시킬수 있다.

- 통지기능
   - Job이 시작되지 않았을 경우
      - 기사, 부기사가 바뀌지 않았을 경우 기사, 부기사, 고객은 Job갱신통지를 받는다. [구현됨]
      - 기사, 부기사가 바뀐 경우
         - 기사, 부기사가 모두 바뀌는 경우 이전 기사, 부기사는 Job삭제 통지를 받고, 새로운 기사, 부기사는 Job창조 통지를 받는다. [구현됨]
         - 기사만 바뀌는 경우 이전 기사는 Job취소통지를 받고 새로운 기사는 Job창조통지를 부기사는 Job갱신통지를 받는다. [구현됨]
         - 부기사만 바뀌는 경우 기사는 Job갱신통지를 이전 부기사는 Job취소통지를 새부기사는 Job창조통지를 받는다. [구현됨]
   - Job이 시작된 경우

### Job삭제 Workflow
- Job은 웹매니저에서 삭제할수 있다.
- 삭제로직
   - 시작하지 않은 Job에 관해서만 삭제를 진행할수 있다. [구현됨]
- 통지기능
   - Job이 삭제되면 기사, 부기사, 고객은 Job취소통지를 받는다. [구현됨]
