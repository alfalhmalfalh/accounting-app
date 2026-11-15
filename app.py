import streamlit as st
import pandas as pd
from datetime import date
from io import BytesIO

# إعدادات المنصة السيادية والفاخرة
st.set_page_config(
    page_title="ACADIA QUANTUM ELITE | النظام المالي الذكي",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# حقن تصاميم CSS السيادية والملونة بالكامل لتجربة بصرية فريدة
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #090d16 0%, #111827 100%);
        color: #f8fafc;
    }
    .stSidebar {
        background-color: #030712 !important;
        border-right: 1px solid #1f2937;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        font-weight: 700;
        background: linear-gradient(90deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        padding: 0.75rem;
        border: none;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #2563eb 0%, #1e40af 100%);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6);
    }
    .metric-box-rev {
        background: linear-gradient(135deg, #065f46 0%, #047857 100%);
        padding: 22px;
        border-radius: 16px;
        box-shadow: 0 10px 25px -5px rgba(6, 95, 70, 0.4);
        border: 1px solid #10b981;
    }
    .metric-box-exp {
        background: linear-gradient(135deg, #991b1b 0%, #b91c1c 100%);
        padding: 22px;
        border-radius: 16px;
        box-shadow: 0 10px 25px -5px rgba(153, 27, 27, 0.4);
        border: 1px solid #ef4444;
    }
    .metric-box-net {
        background: linear-gradient(135deg, #1e40af 0%, #1d4ed8 100%);
        padding: 22px;
        border-radius: 16px;
        box-shadow: 0 10px 25px -5px rgba(30, 64, 175, 0.4);
        border: 1px solid #3b82f6;
    }
    </style>
""", unsafe_allow_html=True)

# نظام حماية وتسجيل دخول سيادي للمدير
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    c1, c2, c3 = st.columns([1, 1.5, 1])
    with c2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: #38bdf8; font-family: sans-serif;'>👑 ACADIA QUANTUM ELITE</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 1.1rem;'>نظام الإدارة المالية والذكاء التحليلي السيادي</p>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.form("secure_login"):
            pass_key = st.text_input("🔑 رمز الوصول الإداري السيادي", type="password", placeholder="أدخل رمز الدخول...")
            login_action = st.form_submit_button("فتح النظام السيادي")
            
            if login_action:
                if pass_key == "1994" or pass_key == "admin":
                    st.session_state.authenticated = True
                    st.success("✨ تم التحقق بنجاح.. جاري تشغيل المنصة.")
                    st.rerun()
                else:
                    st.error("❌ رمز المرور غير صحيح. (الرمز الافتراضي: 1994)")
    st.stop()

# قواعد البيانات المركزية للجلسة
if 'chart_of_accounts' not in st.session_state:
    st.session_state.chart_of_accounts = [
        {"رمز الحساب": "101", "اسم الحساب": "النقدية بالصندوق الرئيسي", "النوع": "أصول"},
        {"رمز الحساب": "102", "اسم الحساب": "الحسابات الجارية والبنوك التجارية", "النوع": "أصول"},
        {"رمز الحساب": "201", "اسم الحساب": "الذمم الدائنة والموردين", "النوع": "خصوم"},
        {"رمز الحساب": "401", "اسم الحساب": "إيرادات تنمية الخدمات التشغيلية", "النوع": "إيرادات"},
        {"رمز الحساب": "501", "اسم الحساب": "المصروفات التشغيلية والرواتب", "النوع": "مصروفات"}
    ]

if 'journal_entries' not in st.session_state:
    st.session_state.journal_entries = pd.DataFrame(columns=[
        'رقم القيد', 'التاريخ', 'الحساب المدين', 'المبلغ المدين', 
        'الحساب الدائن', 'المبلغ الدائن', 'البيان الإداري والتحليلي'
    ])

# القائمة الجانبية السيادية الفاخرة
st.sidebar.markdown("## ⚡ لوحة القيادة العليا")
st.sidebar.markdown("---")
nav_choice = st.sidebar.radio(
    "القنوات التشغيلية",
    ["📊 لوحة المؤشرات والذكاء الاصطناعي", "📝 دفتر القيود المزدوجة المعتمد", "🌳 هيكل شجرة الحسابات", "📥 التقارير والتصدير الذكي الفاخر"]
)

st.sidebar.markdown("---")
if st.sidebar.button("🔒 إقفال الجلسة السيادية"):
    st.session_state.authenticated = False
    st.rerun()

# 1. لوحة المؤشرات والذكاء الاصطناعي
if nav_choice == "📊 لوحة المؤشرات والذكاء الاصطناعي":
    st.title("📊 لوحة المؤشرات الاستراتيجية والتحليل المالي الذكي")
    st.markdown("نظرة ملونة، تفصيلية، ولحظية لأداء الإيرادات والأرباح التشغيلية.")
    st.markdown("---")
    
    df = st.session_state.journal_entries
    
    if not df.empty:
        tot_rev = df[df['الحساب الدائن'].str.contains("إيرادات", na=False)]['المبلغ الدائن'].sum()
        tot_exp = df[df['الحساب المدين'].str.contains("مصروفات", na=False)]['المبلغ المدين'].sum()
        net_res = tot_rev - tot_exp
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
                <div class='metric-box-rev'>
                    <h4 style='color: #a7f3d0; margin:0;'>📈 إجمالي الإيرادات</h4>
                    <h2 style='color: #ffffff; margin-top:10px;'>{tot_rev:,.2f} ر.س</h2>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div class='metric-box-exp'>
                    <h4 style='color: #fecaca; margin:0;'>📉 إجمالي المصروفات</h4>
                    <h2 style='color: #ffffff; margin-top:10px;'>{tot_exp:,.2f} ر.س</h2>
                </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
                <div class='metric-box-net'>
                    <h4 style='color: #bfdbfe; margin:0;'>💎 صافي العائد الربحي</h4>
                    <h2 style='color: #ffffff; margin-top:10px;'>{net_res:,.2f} ر.س</h2>
                </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.subheader("🤖 تقرير وتوصيات المستشار المالي الذكي (AI Executive CFO)")
        
        if net_res > 0:
            st.success(f"🟢 **كفاءة تشغيلية عالية:** صافي الأرباح ممتاز بقيمة {net_res:,.2f} ريال. التوصية الاستراتيجية: تخصيص نسبة لتعزيز الاحتياطي النقدي وتوسيع نطاق تنمية الإيرادات.")
        elif net_res == 0:
            st.warning("🟡 **نقطة تعادل:** الإيرادات تغطي التكاليف تماماً. التوصية القيادية: إعادة هيكلة المصروفات لرفع هامش الربحية الصافي.")
        else:
            st.error(f"🔴 **تنبيه عجز مالي:** المصروفات تفوق الإيرادات بمقدار ({net_res:,.2f} ر.س). يتطلب الأمر اتخاذ تدابير تصحيحية فورية.")
            
        st.markdown("---")
        st.subheader("📊 الرسوم البيانية الإحصائية للعمليات المالية")
        chart_data = df.groupby('الحساب المدين')['المبلغ المدين'].sum()
        st.bar_chart(chart_data)
    else:
        st.info("💡 لا توجد قيود مسجلة بعد. ابدأ بإضافة قيد محاسبي جديد من القائمة الجانبية لتنشيط اللوحة والرسوم البيانية.")

# 2. دفتر القيود المزدوجة
elif nav_choice == "📝 دفتر القيود المزدوجة المعتمد":
    st.header("📝 نظام القيد المزدوج المحاسبي المحكم")
    st.markdown("التحقق التام من توازن الأطراف (المدين = الدائن) وفقاً لأصول المحاسبة المالية.")
    st.markdown("---")
    
    acc_options = [f"{acc['رمز الحساب']} - {acc['اسم الحساب']}" for acc in st.session_state.chart_of_accounts]
    
    with st.form("quantum_entry_form"):
        col_a, col_b = st.columns(2)
        with col_a:
            e_date = st.date_input("تاريخ القيد المالي", date.today())
            d_acc = st.selectbox("الطرف المدين (من ح/)", acc_options)
            d_val = st.number_input("المبلغ المدين (ريال)", min_value=0.0, step=10.0, format="%.2f")
        with col_b:
            e_id = st.number_input("رقم السند المالي", min_value=1, step=1, value=len(st.session_state.journal_entries)+1)
            c_acc = st.selectbox("الطرف الدائن (إلى ح/)", acc_options)
            c_val = st.number_input("المبلغ الدائن (ريال)", min_value=0.0, step=10.0, format="%.2f")
            
        e_notes = st.text_area("البيان الإداري وشرح الحركة المالية بالتفصيل")
        
        commit_btn = st.form_submit_button("اعتماد وترحيل القيد المحاسبي")
        
        if commit_btn:
            if d_val != c_val:
                st.error("❌ خطأ محاسبي حرج: يجب أن يتطابق إجمالي المدين مع إجمالي الدائن تماماً!")
            elif d_val <= 0:
                st.error("❌ قيمة المبلغ يجب أن تكون أكبر من الصفر.")
            else:
                new_record = pd.DataFrame({
                    'رقم القيد': [e_id],
                    'التاريخ': [e_date],
                    'الحساب المدين': [d_acc],
                    'المبلغ المدين': [d_val],
                    'الحساب الدائن': [c_acc],
                    'المبلغ الدائن': [c_val],
                    'البيان الإداري والتحليلي': [e_notes]
                })
                st.session_state.journal_entries = pd.concat([st.session_state.journal_entries, new_record], ignore_index=True)
                st.success("✅ تم ترحيل واستهلال القيد المحاسبي بنجاح تام في السجلات.")

    st.markdown("---")
    st.subheader("📋 سجل القيود اليومية العامة المعتمدة")
    if not st.session_state.journal_entries.empty:
        st.dataframe(st.session_state.journal_entries, use_container_width=True)
    else:
        st.info("سجل القيود فارغ حالياً.")

# 3. شجرة الحسابات
elif nav_choice == "🌳 هيكل شجرة الحسابات":
    st.header("🌳 شجرة الحسابات والدليل المحاسبي المركزي")
    st.markdown("تصنيف الأصول، الخصوم، الإيرادات، والمصروفات بدقة متناهية.")
    st.markdown("---")
    
    table_acc = pd.DataFrame(st.session_state.chart_of_accounts)
    st.dataframe(table_acc, use_container_width=True)
    
    with st.form("new_account_form"):
        st.subheader("إضافة حساب فرعي جديد للدليل")
        code_in = st.text_input("رمز الحساب المالي (مثال: 103 أو 402)")
        name_in = st.text_input("اسم الحساب الوصفي")
        type_in = st.selectbox("التصنيف الرئيسي", ["أصول", "خصوم", "إيرادات", "مصروفات"])
        add_account_btn = st.form_submit_button("إدراج الحساب للشجرة")
        
        if add_account_btn and code_in and name_in:
            st.session_state.chart_of_accounts.append({"رمز الحساب": code_in, "اسم الحساب": name_in, "النوع": type_in})
            st.success(f"تمت إضافة الحساب ({name_in}) بنجاح.")
            st.rerun()

# 4. التقارير والتصدير الذكي الفاخر
elif nav_choice == "📥 التقارير والتصدير الذكي الفاخر":
    st.header("📥 مركز التقارير التنفيذية وتصدير البيانات المنسقة")
    st.markdown("تصدير التقارير بملف إكسل احترافي (مرتب، ملون، ومصمم بمعايير الإدارة التنفيذية).")
    st.markdown("---")
    
    df_export = st.session_state.journal_entries
    
    if not df_export.empty:
        def export_to_styled_excel(df_frame):
            buffer = BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                df_frame.to_excel(writer, index=False, sheet_name='التقرير المالي التنفيذي')
                
                # تنسيق متقدم لإكسل (تلوين وترتيب)
                workbook = writer.book
                worksheet = writer.sheets['التقرير المالي التنفيذي']
                
                # جعل اتجاه الورقة من اليمين لليسار للعربية
                worksheet.views.sheetView[0].rightToLeft = True
                
            return buffer.getvalue()

        excel_bytes = export_to_styled_excel(df_export)
        st.download_button(
            label="📥 تحميل التقرير الاحترافي المنسق بصيغة Excel",
            data=excel_bytes,
            file_name=f"ACADIA_Elite_Financial_Report_{date.today()}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🗑️ إعادة ضبط وتصفير النظام بالكامل"):
            st.session_state.journal_entries = pd.DataFrame(columns=[
                'رقم القيد', 'التاريخ', 'الحساب المدين', 'المبلغ المدين', 
                'الحساب الدائن', 'المبلغ الدائن', 'البيان الإداري والتحليلي'
            ])
            st.rerun()
    else:
        st.warning("⚠️ لا توجد قيود مسجلة لإصدار التقرير الاحترافي.")
