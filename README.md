# B00TJUNGLE Project

> 코로나로 삭막해진 2021년 설날 연휴동안 시간때우기로 시작한 프로젝트 내용을 정리한 페이지입니다. (현재 진행중 👀👀👀)

![preview](https://user-images.githubusercontent.com/4216651/108615618-5ad0cc80-7449-11eb-9a63-22a4cf2c3cf4.gif)

## 0. 대표 적용 기술 스택

> `Next.js` , `TypeScript`, `Redux Toolkit`, `Styled-components`, `MaterialUI`, `jest`, `GraphQL`, `Prisma`, `Flask`

## 1. 설치

- `npm install`을 통해 패키지를 설치합니다.

```console
$ npm install
```

## 2. 실행

- `npm run dev`를 통해 `dev server`를 실행합니다.
- `npm run build`를 통해 빌드를 실행합니다.

```console
// dev server
$ npm run dev

// build
$ npm run build
```

## 3. 테스트 (예정)

- `npm run test` 를 통해 `jest`를 실행합니다.

```console
$ npm run test
```

## 4. 프로젝트 모듈 소개

```console
.
├── pages/
│   ├── api
│   ├── bootcamps/
│   │   ├── [name].tsx
│   │   └── index.tsx
│   ├── _app.tsx
│   ├── _docuemnt.tsx
│   ├── 404.tsx
│   └── index.tsx
├── public/
├── src/
│   ├── api/
│   │   ├── Bootcamp/
│   │   ├── Ranking/
│   │   └── index.ts
│   ├── common/
│   │   ├── images/
│   │   └── theme/
│   │       ├── Devices.ts
│   │       ├── Global.ts
│   │       ├── index.ts
│   │       ├── Mixin.ts
│   │       └── MUI.ts
│   ├── components/
│   │   ├── Bootcamp/
│   │   ├── Home/
│   │   ├── List/
│   │   ├── Footer.tsx
│   │   └── Navbar.tsx
│   ├── layout/
│   ├── store/
│   │   ├── actions/
│   │   │   ├── bootcampActions/
│   │   │   ├── rankingActions/
│   │   │   └── index.ts
│   │   ├── reducer/
│   │   │   ├── bootcampSlice/
│   │   │   ├── rankingSlice/
│   │   │   └── index.ts
│   │   └── index.ts
│   ├── styles/
│   └── template/
│       ├── Bootcamp/
│       ├── Ranking/
│       └── index.ts
├── .babelrc
├── .env.local
├── index.d.ts
├── module.d.ts
├── next-env.d.ts
├── next.config.js
├── package-lock.json
├── package.json
└── tsconfig.json
```

1. `pages` 폴더 안에 `Next.js`로 구현된 개별 페이지 뷰를 관리합니다.

2. `public` 에서는 public하게 쓰일 `resource`들을 관리합니다. (e.g. `Mockdata` 등)

3. `src` 에서 나머지 리소스들을 관리하며 `@/*` 해당하는 절대경로입니다. (`tsconfig.json` 참고)

4. `src/api`는 외부요청 `API`를 관리하는 모듈이고 세부모듈로 나뉘어져 있습니다.

   - `@/api`을 통해 세부모듈 포함 모든 `api`에 접근 가능합니다.

5. `src/common`은 공통으로 쓰일 이미지(`src/common/images`), 테마(`src/common/theme`)를 관리하는 모듈입니다.

   - `theme` 모듈 안에는 `responsive`를 위한 `device` 조건 모듈(`Devices.ts`), `style reset`을 포함한 전체 공통 테마 모듈(`Global.ts`), 자주쓰는 스타일 `API`를 모아놓은 모듈(`Mixin.ts`), `Material UI` 공통 조건 모듈(`MUI.ts`)로 구성되어 있으며 그외 공통 스타일과 함께 `index.ts`에서 전부 모아서 내보내줍니다. `@/common/theme` 경로로 모든 하위 모듈에 접근 가능합니다.
   - `@/common/images` 경로로 폴더 내 모든 이미지에 접근 가능합니다.

6. `src/components`는 `pages`에 필요한 페이지에 직접적으로 연관된 `component`들을 관리하는 모듈입니다.

   - `@/components/[해당모듈]`로 접근 가능합니다.

7. `src/layout`은 `next.js`에 전체적으로 적용되는 `API`들 (e.g `Global styled-component`, `Redux` 등)을 관리하는 모듈입니다.

   - `@/layout`으로 접근합니다.

8. `src/store`은 `redux store`를 관리하는 모듈입니다. `Redux Toolkit`을 이용하여 구성하였으며 크롬앱 `Redux DevTool`와 함께 이용하면 스토어 상태를 쉽게 확인할 수 있습니다. `actions`에는 비동기(`Redux-Thunk`)를 포함한 `action` 함수를 관리하며 `reducer`는 각 `slice` 상태와 해당하는 순수함수들이 위치해있습니다.

   - `@/store`로 접근 가능하며, `action`의 경우 `@/store/actions`로 하위 `action`까지 전부 접근 가능합니다.

9. `src/styles`는 각각 뷰와 컴포넌트에 해당하는 `styled-components` 관리하는 모듈입니다.

   - `@/styles/[해당모듈]`로 접근합니다.

10. `src/template`은 `TypeScript`의 타입을 관리해주는 모듈입니다.

    - `@/template`을 통해 하위 모듈 타입까지 전부 접근 가능합니다.

11. `.env.local`에서 `API Endpoint` 를 관리합니다.

## 5. 설치된 패키지

```json
"dependencies": {
  "axios": "^0.21.1",
  "core-js": "^3.8.3",
  "next": "10.0.6",
  "react": "17.0.1",
  "react-dom": "17.0.1",
  "react-redux": "^7.2.2",
  "styled-components": "^5.2.1"
},
"devDependencies": {
  "@babel/core": "^7.12.13",
  "@babel/plugin-transform-runtime": "^7.12.15",
  "@babel/preset-env": "^7.12.13",
  "@babel/runtime-corejs3": "^7.12.13",
  "@material-ui/core": "^4.11.3",
  "@material-ui/icons": "^4.11.2",
  "@material-ui/lab": "^4.0.0-alpha.57",
  "@reduxjs/toolkit": "^1.5.0",
  "@types/node": "^14.14.25",
  "@types/react": "^17.0.1",
  "@types/react-redux": "^7.1.16",
  "@types/redux-logger": "^3.0.8",
  "@types/styled-components": "^5.1.7",
  "babel-plugin-styled-components": "^1.12.0",
  "next-images": "^1.7.0",
  "redux-logger": "^3.0.6",
  "typescript": "^4.1.5"
},
```

## 6. 기타 참고 사항

### 모듈 관리 방법 예시 (`Type` 호출 방법)

1. `Ranking` 관련된 모듈을 `@/template/Ranking`으로 접근할수 있도록 `/src/template/Ranking/index.ts`을 다음과 같이 구성합니다.

#### /src/template/Ranking/index.ts

```ts
export declare module RankingType {
  // other types...

  export interface RankingState {
    rankings: Rankings;
    isLoading: boolean;
    error: string | null;
  }

  // other types...
}
```

2.  이를 `@/template`로만 접근할수 있도록 `/src/template/index.ts`를 다음과 같이 구성합니다.

#### /src/template/index.ts

```ts
// ...etc

export type { RankingType } from '@/template/Ranking';
export type { BootcampType } from '@/template/Bootcamp';

// ...etc
```

3. 다음과 같이 원하는 타입을 불러올 수 있습니다.

#### /src/store/reducer/rankingSlice/index.ts

```ts
import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { rankingActions } from '@/store/actions';
import { RankingType } from '@/template';

// SECTION state
const initialState: RankingType.RankingState = {
  rankings: [],
  isLoading: false,
  error: null,
};

// SECTION reducers
const reducers = {
  getRankingStart: rankingActions.startLoading,
  getRankingSuccesss(
    state: RankingType.RankingState,
    action: PayloadAction<RankingType.Rankings>
  ) {
    state.rankings = action.payload;
    state.isLoading = false;
    state.error = null;
  },
  getRankingFailed: rankingActions.loadingFailed,
};

// SECTION slices
const rankingSlice = createSlice({
  name: 'ranking',
  initialState,
  reducers,
  extraReducers: (builder) => {},
});

export const {
  getRankingStart,
  getRankingFailed,
  getRankingSuccesss,
} = rankingSlice.actions;

export default rankingSlice.reducer;
```