// 우편번호 찾기 찾기 화면을 넣을 element
var element_wrap = document.getElementById('wrap');

function foldDaumPostcode() {
    // iframe을 넣은 element를 안보이게 한다.
    element_wrap.style.display = 'none';
}

function sample3_execDaumPostcode() {
    // 현재 scroll 위치를 저장해놓는다.
    var currentScroll = Math.max(document.body.scrollTop, document.documentElement.scrollTop);
    new daum.Postcode({
        oncomplete: function(data) {
            // 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.

            // 각 주소의 노출 규칙에 따라 주소를 조합한다.
            // 내려오는 변수가 값이 없는 경우엔 공백('')값을 가지므로, 이를 참고하여 분기 한다.
            var fullAddr = data.address; // 최종 주소 변수
            var extraAddr = ''; // 조합형 주소 변수

            // 기본 주소가 도로명 타입일때 조합한다.
            if(data.addressType === 'R'){
                //법정동명이 있을 경우 추가한다.
                if(data.bname !== ''){
                    extraAddr += data.bname;
                }
                // 건물명이 있을 경우 추가한다.
                if(data.buildingName !== ''){
                    extraAddr += (extraAddr !== '' ? ', ' + data.buildingName : data.buildingName);
                }
                // 조합형주소의 유무에 따라 양쪽에 괄호를 추가하여 최종 주소를 만든다.
                fullAddr += (extraAddr !== '' ? ' ('+ extraAddr +')' : '');
            }

            // 우편번호와 주소 정보를 해당 필드에 넣는다.
            document.getElementById('id_postcode').value = data.zonecode; //5자리 새우편번호 사용
            document.getElementById('id_address1').value = fullAddr;

            // iframe을 넣은 element를 안보이게 한다.
            // (autoClose:false 기능을 이용한다면, 아래 코드를 제거해야 화면에서 사라지지 않는다.)
            element_wrap.style.display = 'none';

            // 우편번호 찾기 화면이 보이기 이전으로 scroll 위치를 되돌린다.
            document.body.scrollTop = currentScroll;
        },
        // 우편번호 찾기 화면 크기가 조정되었을때 실행할 코드를 작성하는 부분. iframe을 넣은 element의 높이값을 조정한다.
        onresize : function(size) {
            element_wrap.style.height = size.height+'px';
        },
        width : '100%',
        height : '100%'
    }).embed(element_wrap);

    // iframe을 넣은 element를 보이게 한다.
    element_wrap.style.display = 'block';
}

function form_submit(){
    if( $(":checked").length == 0){
        alert('최소한 하나 이상의 샘플을 선택해주세요. 제품 옆의 체크박스를 누르면 선택됩니다.');
        return;
    }

    if( $('#id_name').val()=='' ){
        alert('성함을 입력해주세요.');
        $('#id_name').focus();
        return;
    }

    if( $('#id_password').val()=='' ){
        alert('비밀번호를 입력해주세요.');
        $('#id_password').focus();
        return;
    }

    if( $('#id_phone').val()=='' ){
        alert('연락처를 입력해주세요.');
        $('#id_phone').focus();
        return;
    }

    if( $('#id_postcode').val()=='' ){
        alert('우편번호를 입력해주세요.');
        $('#postcode_btn').click();
        return;
    }

    if( $('#id_address1').val()=='' ){
        alert('기본주소를 입력해주세요.');
        $('#id_address1').focus();
        return;
    }

    if( $('#id_address2').val()=='' ){
        alert('상세주소를 입력해주세요.');
        $('#id_address2').focus();
        return;
    }

    $('#sample_request_form').submit();
}

var limit = 3;
$('input.sample_list').on('change', function(evt) {
    console.log($('[name="sample_list"]:checked').length);
   if($('[name="sample_list"]:checked').length > limit) {
    alert('샘플은 3개까지 선택 가능합니다.');
       this.checked = false;
   }
});

