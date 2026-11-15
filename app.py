import streamlit as st
import pandas as pd
from datetime import date
from io import BytesIO

# إعدادات المنصة السيادية والفاخرة
st.set_page_config(
    page_title="ACADIA QUANTUM | النظام المالي والذكي",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# حقن تصاميم CSS السيادية والفاخرة بالكامل لضمان مظهر غير تقليدي (Glassmorphism & Executive UI)
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    .stSidebar {
        background-color: #090d16 !important;
        border-right: 1px solid #1e293b;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        font-weight: 700;
        background: linear-gradient(90deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        padding: 0.75rem;
        border: none;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #2563eb 0%, #1e40af 100%);
        box-shadow: 0 6px 16px rgba(59, 130, 246, 0.5);
    }
    .executive-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(12px);
        padding: 24px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
        margin-bottom: 20px;
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
        st.markdown("<h1 style='text-align: center; color: #38bdf8; font-family: sans-serif;'>⚡ ACADIA QUANTUM</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 1.1rem;'>بوابة الإدارة المالية والتحليل الذكي السيادية</p>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.form("secure_login"):
            pass_key = st.text_input("🔑 رمز الوصول الإداري السيادي", type="password", placeholder="أدخل الرمز هنا...")
            login_action = st.form_submit_button("مصادقة الدخول الآمن")
            
            if login_action:
                if pass_key == "1994" or pass_key == "admin":
                    st.session_state.authenticated = True
                    st.success("✨ تم التحقق من الهوية السيادية بنجاح.. جاري تهيئة النظام.")
                    st.rerun()
                else:
                    st.error("❌ رمز الوصول غير صحيح. (الرمز الافتراضي: 1994)")
    st.stop()

# قواعد البيانات المركزية للجلسة
if 'chart_of_accounts' not in st.session_state:
    st.session_state.chart_of_accounts = [
        {"رمز الحساب": "101", "اسم الحساب": "النقدية بالصندوق الرئيسي", "النوع": "أصول"},
        {"رمز الحساب": "102", "اسم الحساب": "الحسابات الجارية والبنوك", "النوع": "أصول"},
        {"رمز الحساب": "201", "اسم الحساب": "الذمم الدائنة والموردين", "النوع": "خصوم"},
        {"رمز الحساب": "401", "اسم الحساب": "إيرادات تنمية الخدمات التشغيلية", "النوع": "إيرادات"},
        {"رمز الحساب": "501", "اسم الحساب": "المصروفات التشغيلية والعمومية", "النوع": "مصروفات"}
    ]

if 'journal_entries' not in st.session_state:
    st.session_state.journal_entries = pd.DataFrame(columns=[
        'رقم القيد', 'التاريخ', 'الحساب المدين', 'المبلغ المدين', 
        'الحساب الدائن', 'المبلغ الدائن', 'البيان الإداري والتحليلي'
    ])

# القائمة الجانبية السيادية
st.sidebar.markdown("## 🛡️ لوحة القيادة العليا")
st.sidebar.markdown("---")
nav_choice = st.sidebar.radio(
    "القنوات التشغيلية",
    ["📊 لوحة القيادة والذكاء الاصطناعي", "📝 دفتر القيود المزدوجة المعتمد", "🌳 هيكل شجرة الحسابات", "📥 التقارير والتصدير التنفيذي"]
)

st.sidebar.markdown("---")
if st.sidebar.button("🔒 إقفال الجلسة السيادية"):
    st.session_state.authenticated = False
    st.rerun()

# 1. لوحة القيادة والذكاء الاصطناعي
if nav_choice == "📊 لوحة القيادة والذكاء الاصطناعي":
    st.title("📊 لوحة المؤشرات الاستراتيجية والذكاء المالي")
    st.markdown("رؤية تحليلية متقدمة ولحظية لتدفقات الإيرادات والأداء التشغيلي.")
    st.markdown("---")
    
    df = st.session_state.journal_entries
    
    if not df.empty:
        tot_rev = df[df['الحساب الدائن'].str.contains("إيرادات", na=False)]['المبلغ الدائن'].sum()
        tot_exp = df[df['الحساب المدين'].str.contains("مصروفات", na=False)]['المبلغ المدين'].sum()
        net_res = tot_rev - tot_exp
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
                <div class='executive-card'>
                    <h4 style='color: #38bdf8; margin:0;'>إجمالي الإيرادات</h4>
                    <h2 style='color: #ffffff; margin-top:10px;'>{tot_rev:,.2f} ر.س</h2>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div class='executive-card'>
                    <h4 style='color: #f43f5e; margin:0;'>إجمالي المصروفات</h4>
                    <h2 style='color: #ffffff; margin-top:10px;'>{tot_exp:,.2f} ر.س</h2>
                </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
                <div class='executive-card'>
                    <h4 style='color: #10b981; margin:0;'>صافي العائد التشغيلي</h4>
                    <h2 style='color: #ffffff; margin-top:10px;'>{net_res:,.2f} ر.س</h2>
                </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("🤖 تحليل المستشار المالي السيادي (AI Executive CFO)")
        
        if net_res > 0:
            st.success(f"🟢 **مؤشر كفاءة عالي:** صافي الربح يحقق عائداً بـ {net_res:,.2f} ريال. التوصية القيادية: توجيه 20% لتعزيز الاحتياطي النقدي وتوسيع قنوات تنمية الإيرادات.")
        elif net_res == 0:
            st.warning("🟡 **مؤشر تعادل تشغيلي:** الإيرادات تتطابق مع المصروفات تماماً. التوصية: إعادة تقييم كفاءة التكاليف التشغيلية لزيادة الهامش الربحي.")
        else:
            st.error(f"🔴 **تنبيه عجز استراتيجي:** المصروفات تفوق الإيرادات بمقدار ({net_res:,.2f} ر.س). يتطلب الأمر تدخلاً فورياً لإعادة هيكلة المصاريف.")
            
        st.markdown("---")
        st.subheader("📈 التحليل البصري لحركات الحسابات")
        chart_data = df.groupby('الحساب المدين')['المبلغ المدين'].sum()
        st.bar_chart(chart_data)
    else:
        st.info("💡 لا توجد قيود مالية مسجلة بعد. ابدأ بترحيل قيد مزدوج من القائمة الجانبية لتنشيط اللوحة الاستراتيجية.")

# 2. دفتر القيود المزدوجة
elif nav_choice == "📝 دفتر القيود المزدوجة المعتمد":
    st.header("📝 نظام القيد المزدوج المحاسبي المحكم")
    st.markdown("ضمان التوازن التام بين الأطراف المدينة والدائنة وفق الأصول المحاسبية الصارمة.")
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
            
        e_notes = st.text_area("البيان الإداري وشرح الحركة المالية")
        
        commit_btn = st.form_submit_button("اعتماد وترحيل القيد للدفتر العام")
        
        if commit_btn:
            if d_val != c_val:
                st.error("❌ خطأ محاسبي سيادي: يجب أن يتطابق إجمالي المدين مع إجمالي الدائن تماماً!")
            elif d_val <= 0:
                st.error("❌ قيمة المبلغ المدين/الدائن يجب أن تكون أكبر من الصفر.")
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
                st.success("✅ تم اعتماد وترحيل القيد المحاسبي بنجاح تام وإدراجه في السجلات.")

    st.markdown("---")
    st.subheader("📋 سجل اليومية العامة المعتمد")
    if not st.session_state.journal_entries.empty:
        st.dataframe(st.session_state.journal_entries, use_container_width=True)
    else:
        st.info("سجل القيود فارغ حالياً.")

# 3. شجرة الحسابات
elif nav_choice == "🌳 هيكل شجرة الحسابات":
    st.header("🌳 شجرة الحسابات والدليل المحاسبي المركزي")
    st.markdown("التصنيف الهيكلي الشامل للأصول، الخصوم، الإيرادات، والمصروفات.")
    st.markdown("---")
    
    table_acc = pd.DataFrame(st.session_state.chart_of_accounts)
    st.dataframe(table_acc, use_container_width=True)
    
    with st.form("new_account_form"):
        st.subheader("إضافة حساب فرعي جديد للدليل")
        code_in = st.text_input("رمز الحساب المالي (مثال: 103 أو 402)")
        name_in = st.text_input("اسم الحساب الوصفي")
        type_in = st.selectbox("التصنيف الرئيسي", ["أصول", "خصوم", "إيرادات", "مصروفات"])
        add_account_btn = st.form_submit_button("إدراج الحساب في الشجرة")
        
        if add_account_btn and code_in and name_in:
            st.session_state.chart_of_accounts.append({"رمز الحساب": code_in, "اسم الحساب": name_in, "النوع": type_in})
            st.success(f"تمت إضافة الحساب ({name_in}) بنجاح.")
            st.rerun()

# 4. التقارير والتصدير الذكي
elif nav_choice == "📥 التقارير والتصدير التنفيذي":
    st.header("📥 مركز التقارير التنفيذية وتصدير البيانات")
    st.markdown("تصدير السجلات الرسمية بدقة متناهية بصيغة Excel المعتمدة.")
    st.markdown("---")
    
    df_export = st.session_state.journal_entries
    
    if not df_export.empty:
        def export_to_excel(df_frame):
            buffer = BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                df_frame.to_excel(writer, index=False, sheet_name='سجل القيود السيادية')
            return buffer.getvalue()

        excel_data_bytes = export_to_excel(df_export)
        st.download_button(
            label="📥 تحميل التقرير المالي الشامل بصيغة Excel",
            data=excel_data_bytes,
            file_name=f"ACADIA_Quantum_Report_{date.today()}.xlsx",
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
        st.warning("⚠️ لا توجد قيود مسجلة لإصدار التقرير التنفيذي.")
